import logging
import unittest
from pathlib import Path

from pages.home_page import HomePage
from pages.login_page import LoginPage

from utils.csv_reader import CSVReader
from utils.config_reader import ConfigReader
from utils.driver_factory import DriverFactory
from utils.screenshot import Screenshot


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA = CSVReader.read_data(PROJECT_ROOT / "test_data" / "test_data.csv")


class LoginUnittest(unittest.TestCase):
    def setUp(self):
        config = ConfigReader()
        self.base_url = config.get("DEFAULT", "base_url")
        self.driver = DriverFactory.create_driver(
            config.get("DEFAULT", "browser")
        )
        self.driver.implicitly_wait(
            int(config.get("DEFAULT", "implicit_wait"))
        )

    def tearDown(self):
        if not getattr(self, "driver", None):
            return

        try:
            if self._outcome and not self._outcome.success:
                try:
                    Screenshot.capture(self.driver, self.id().split(".")[-1])
                except Exception:
                    logging.getLogger(__name__).exception(
                        "Failed to capture a screenshot for %s",
                        self.id()
                    )
        finally:
            self.driver.quit()

    def test_invalid_login(self):
        credentials = next(
            row for row in DATA if row["test_case"] == "invalid_login"
        )
        self.driver.get(self.base_url)
        HomePage(self.driver).click_login()

        login_page = LoginPage(self.driver)
        login_page.login(credentials["email"], credentials["password"])

        self.assertEqual(
            login_page.get_error_message(),
            "Your email or password is incorrect!"
        )


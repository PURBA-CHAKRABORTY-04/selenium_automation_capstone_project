import os
from pathlib import Path

import pytest

from pages.home_page import HomePage
from pages.login_page import LoginPage
from utils.csv_reader import CSVReader
from utils.config_reader import ConfigReader
from utils.screenshot import Screenshot

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA = CSVReader.read_data(PROJECT_ROOT / "test_data" / "test_data.csv")


def get_case(test_case):
    return next(row for row in DATA if row["test_case"] == test_case)


valid_credentials = get_case("valid_login")
valid_email = os.getenv(
    "AUTOMATIONEXERCISE_EMAIL",
    valid_credentials["email"]
).strip()
valid_password = os.getenv(
    "AUTOMATIONEXERCISE_PASSWORD",
    valid_credentials["password"]
).strip()
has_valid_credentials = (
    bool(valid_email and valid_password)
    and valid_email != "valid_email@example.com"
    and valid_password != "valid_password"
)


def open_login_page(driver):
    config = ConfigReader()
    driver.get(config.get("DEFAULT", "base_url"))
    HomePage(driver).click_login()


def test_invalid_login(driver):
    credentials = get_case("invalid_login")
    open_login_page(driver)

    login_page = LoginPage(driver)
    login_page.login(credentials["email"], credentials["password"])

    assert login_page.get_error_message() == (
        "Your email or password is incorrect!"
    )
    Screenshot.capture(driver, "test_invalid_login")


@pytest.mark.skipif(
    not has_valid_credentials,
    reason=(
        "Set real valid-login credentials in test_data.csv or the "
        "AUTOMATIONEXERCISE_EMAIL and AUTOMATIONEXERCISE_PASSWORD "
        "environment variables."
    )
)
def test_valid_login(driver):
    open_login_page(driver)
    login_page = LoginPage(driver)
    login_page.login(valid_email, valid_password)

    assert login_page.is_logged_in()
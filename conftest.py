import logging

import pytest

from utils.driver_factory import DriverFactory
from utils.config_reader import ConfigReader
from utils.screenshot import Screenshot


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    setattr(item, f"rep_{call.when}", outcome.get_result())


@pytest.fixture
def driver(request):

    config = ConfigReader()

    browser = config.get(
        "DEFAULT",
        "browser"
    )

    driver = DriverFactory.create_driver(
        browser
    )

    driver.implicitly_wait(
        int(
            config.get(
                "DEFAULT",
                "implicit_wait"
            )
        )
    )

    try:
        yield driver
    finally:
        report = getattr(request.node, "rep_call", None)
        if report and report.failed:
            try:
                Screenshot.capture(driver, request.node.name)
            except Exception:
                logging.getLogger(__name__).exception(
                    "Failed to capture a screenshot for %s",
                    request.node.name
                )
        driver.quit()
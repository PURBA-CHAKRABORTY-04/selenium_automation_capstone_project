from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


class DriverFactory:

    @staticmethod
    def create_driver(browser="chrome"):

        if browser.lower() == "chrome":

            options = Options()
            options.add_argument("--start-maximized")

            service = Service(
                ChromeDriverManager().install()
            )

            driver = webdriver.Chrome(
                service=service,
                options=options
            )

            return driver

        else:
            raise ValueError(
                f"Unsupported browser: {browser}"
            )
        #instead of putting:driver = webdriver.Chrome() inside every test, we have one reusable driver factory.


if __name__ == "__main__":
    driver = DriverFactory.create_driver()
    try:
        input("Chrome is open. Press Enter to close it...")
    finally:
        driver.quit()
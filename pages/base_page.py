from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click(self, locator):
        element = self.wait.until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    def enter_text(self, locator, text):
        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )
        return element.text

    def is_displayed(self, locator):
        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )
        return element.is_displayed()

    def get_title(self):
        return self.driver.title

    def get_current_url(self):
        return self.driver.current_url
    #foundation of base page model
    #every page needs operations like click, enter_text etc.
    #instead of duplicating them in every page we write them once
    
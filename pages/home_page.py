from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):

    LOGIN_BUTTON = (
        By.XPATH,
        "//a[contains(text(),'Signup / Login')]"
    )

    PRODUCTS_BUTTON = (
        By.XPATH,
        "//a[contains(text(),'Products')]"
    )

    def click_login(self):
        self.click(self.LOGIN_BUTTON)

    def click_products(self):
        self.click(self.PRODUCTS_BUTTON)
        #this class represents the home page and can locate login buttons etc etc by xpath
        
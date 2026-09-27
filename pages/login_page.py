from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):

    EMAIL_FIELD = (
        By.XPATH,
        "//input[@data-qa='login-email']"
    )

    PASSWORD_FIELD = (
        By.XPATH,
        "//input[@data-qa='login-password']"
    )

    LOGIN_BUTTON = (
        By.XPATH,
        "//button[@data-qa='login-button']"
    )

    LOGGED_IN_USER = (
        By.XPATH,
        "//a[contains(text(),'Logged in as')]"
    )

    ERROR_MESSAGE = (
        By.XPATH,
        "//p[contains(text(),'Your email or password is incorrect!')]"
    )

    def enter_email(self, email):
        self.enter_text(self.EMAIL_FIELD, email)

    def enter_password(self, password):
        self.enter_text(self.PASSWORD_FIELD, password)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)

    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()

    def is_logged_in(self):
        return self.is_displayed(self.LOGGED_IN_USER)

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)
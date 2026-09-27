from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SearchPage(BasePage):

    SEARCH_BOX = (
        By.ID,
        "search_product"
    )

    SEARCH_BUTTON = (
        By.ID,
        "submit_search"
    )

    SEARCHED_PRODUCTS = (
        By.XPATH,
        "//h2[contains(text(),'Searched Products')]"
    )

    PRODUCT_NAMES = (
        By.XPATH,
        "//div[contains(@class,'productinfo')]//p"
    )

    def search_product(self, product_name):
        self.enter_text(
            self.SEARCH_BOX,
            product_name
        )
        self.click(self.SEARCH_BUTTON)

    def is_search_results_displayed(self):
        return self.is_displayed(
            self.SEARCHED_PRODUCTS
        )

    def get_product_names(self):
        elements = self.driver.find_elements(
            *self.PRODUCT_NAMES
        )

        return [
            element.text for element in elements
        ]
from pathlib import Path

from pages.home_page import HomePage
from pages.search_page import SearchPage

from utils.csv_reader import CSVReader
from utils.config_reader import ConfigReader


data = CSVReader.read_data(
    Path(__file__).resolve().parents[1]
    / "test_data"
    / "test_data.csv"
)

search_data = next(
    item for item in data
    if item["test_case"] == "search_product"
)


def test_product_search(driver):

    config = ConfigReader()

    driver.get(
        config.get(
            "DEFAULT",
            "base_url"
        )
    )

    home_page = HomePage(driver)
    search_page = SearchPage(driver)

    home_page.click_products()

    search_page.search_product(
        search_data["product"]
    )

    assert search_page.is_search_results_displayed()

    products = search_page.get_product_names()

    assert len(products) > 0
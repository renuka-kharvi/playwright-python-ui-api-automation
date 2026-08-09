from playwright.sync_api import Page
from pages.home_page import HomePage
from pages.search_page import SearchPage
from pages.item_page import ItemPage
from playwright.sync_api import expect
import pytest
from utils.data_reader import read_json_data
from utils.logger import get_logger

logger=get_logger(__name__)

# read data drom test data json file
card_data=read_json_data("testdata/ui_data/add_to_cart.json")
@pytest.mark.ui
class TestAddToCard:
    @pytest.mark.parametrize("data",[card_data["cart"]])
    def test_num_item_in_cart(self,page:Page,data):
        """
        Scenario 1 – Verify item can be added to Cart
        """
        logger.info("cart verify test started")
        home_page=HomePage(page)
        search_page=SearchPage(page)
        
        home_page.search_products(data["search_product"])
        # click product will open new tab item_page returing new tab page
        new_item_page=search_page.item_page()

        logger.info(f" Current URL: {new_item_page.url}")
        logger.info(f"Title:{ new_item_page.title()}")
        new_home_page=HomePage(new_item_page)
        item_page=ItemPage(new_item_page)
        item_page.click_add_to_cart()
        expect(item_page.added_to_cart_close).to_be_visible(timeout=10000)
        
        item_page.click_added_to_cart_close()
       
        expect(new_home_page.num_items()).to_have_text(str(data["expected_cart_count"]))

        logger.info("cart verify test ended")

        



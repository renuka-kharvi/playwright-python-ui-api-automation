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
        logger.info("cart verification test started")
        home_page=HomePage(page)
        search_page=SearchPage(page)

        # Step 1: Search for the product.
        home_page.search_products(data["search_product"])

        # Step 2: Open the first product.
        # This opens the product in a new tab/page
        item_page_tab=search_page.item_page()

        logger.info(f" Current URL: {item_page_tab.url}")
        logger.info(f"Title:{ item_page_tab.title()}")

        # Step3 : Create Page Objects using the new tab.
        new_home_page=HomePage(item_page_tab)
        item_page=ItemPage(item_page_tab)

        # Step 4: Verify "Added to cart" confirmation is displayed.
        item_page.click_add_to_cart()

        #step 5 Verify "Added to cart" confirmation is displayed.
        expect(item_page.added_to_cart_close).to_be_visible(timeout=10000)

       # Step 6: Close the "Added to cart" confirmation.
        item_page.click_added_to_cart_close()
       #Step 7: Verify cart count.
        expect(new_home_page.num_items()).to_have_text(str(data["expected_cart_count"]))

        logger.info("Cart verification test completed successfully")

        



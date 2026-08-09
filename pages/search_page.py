from pages.base_page import BasePage
from utils.logger import get_logger
class SearchPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.logger=get_logger(__name__)

        #-----------------------------------------------------
        # search page locator
        #-------------------------------------------------------
        self.first_search_product=self.page.locator(".s-card__link")


    #-----------------------------------------------------
    # click on first product its opening new tab, this method returing new tab page to perform action on new page
    #-------------------------------------------------------
    def item_page(self):
        self.logger.info(f'clicking first product ,returning new tab page')
        with self.page.context.expect_page() as page_info:
            self.first_search_product.nth(0).click(force=True)

        new_page = page_info.value
        new_page.wait_for_load_state()

        return new_page
    



    
    
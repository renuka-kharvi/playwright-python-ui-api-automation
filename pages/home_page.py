from pages.base_page import BasePage
from playwright.sync_api import Page

class HomePage(BasePage):
    def __init__(self,page:Page):
        self.page=page
        super().__init__(page)
        #-----------------------------------------------------
        # locator of home page of the application
        #-------------------------------------------------------
        self.search_box=self.page.get_by_role("combobox",name="Search for anything")
        self.search_button=self.page.get_by_role("button",name="Search",exact=True)
        self.num_item=self.page.locator("span.badge.badge--circle.gh-badge")


    #-----------------------------------------------------
    # searhc product to add to cart
    #-------------------------------------------------------
    def search_products(self,product):
        self.fill(self.search_box,product)
        self.click(self.search_button)

    #-----------------------------------------------------
    # returing number of item in card element
    #-------------------------------------------------------
    def num_items(self):
        return self.num_item
    
        
        


    

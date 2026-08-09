from pages.base_page import BasePage

class ItemPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        #-----------------------------------------------------
        # locator of item/product of the application
        #-------------------------------------------------------
        self.add_to_cart=self.page.get_by_role("button",name="Add to cart")
        self.see_in_cart=self.page.get_by_role("button",name="See in cart")
        self.added_to_cart_close=self.page.locator("button.lightbox-dialog__close:visible")


    #-----------------------------------------------------
    # click add to cart button
    #-------------------------------------------------------
    def click_add_to_cart(self):
       self.add_to_cart.click()
       
    #-----------------------------------------------------
    # click see in cart button
    #-------------------------------------------------------
    def click_see_in_cart(self):
        self.click(self.see_in_cart)

    #-----------------------------------------------------
    # click add to cart close button
    #-------------------------------------------------------
    def click_added_to_cart_close(self):
        self.click(self.added_to_cart_close)


    
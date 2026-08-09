from playwright.sync_api import Page
class BasePage:
    def __init__(self,page:Page):
        self.page=page

    #-----------------------------------------------------
    # below methods are comman helper methods for perform action
    #-------------------------------------------------------
    def click(self, element):
        element.click()

    def fill(self, element, value):
        element.clear()
        element.fill(value)

    def type(self, element, value):
        element.type(value)

    def hover(self, element):
        element.hover()

    def press(self, element, key):
        element.press(key)

    def check(self, element):
        element.check()

    def uncheck(self, element):
        element.uncheck()

    def select(self, element, value):
        element.select_option(value)

    def get_text(self, element):
        return element.text_content()

    def is_visible(self, element):
        return element.is_visible()


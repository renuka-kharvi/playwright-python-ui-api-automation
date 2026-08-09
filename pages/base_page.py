from playwright.sync_api import Page
from utils.logger import get_logger


class BasePage:
    def __init__(self,page:Page):
        self.page=page
        self.logger=get_logger(__name__)

    #-----------------------------------------------------
    # below methods are comman helper methods for perform action
    #-------------------------------------------------------
    def click(self, locator):
        try:
            # Log the action before execution.
            self.logger.info(f"Clicking element: {locator}")
            locator.click()
        except Exception as error:

            # Log the actual error.
            self.logger.error(f"Click failed for {locator}: {error}")
            raise


    def fill(self, locator, value):
        try:
            self.logger.info(f"Filling element with value: {value}")
            locator.clear()
            locator.fill(value)
        except Exception as error:

            self.logger.error(f"Fill failed for {locator}: {error}")
            raise


    def type(self, locator, value):
        try:
            self.logger.info(f"type element with value: {value}")
            locator.type(value)

        except Exception as error:
            self.logger.error(f"type failed for {locator}: {error}")
            raise
        

    def hover(self, locator):
        try:
            self.logger.info(f"hover to element with locator: {locator}")
            locator.hover()
        except Exception as error:
            self.logger.error(f"hover failed for {locator}: {error}")
            raise

    def press(self, locator, key):
        try:
            self.logger.info(f"Pressing key {key}")
            locator.focus()
            locator.press(key)
        except Exception as error:
            self.logger.error(f"press key element with locator: {locator}: {error}")
            raise

    def check(self, locator):
        try:
            self.logger.info(f"check the element with locator: {locator}")
            locator.check()
        except Exception as error:
            self.logger.error(f"check failed for {locator}: {error}")
            raise

    def uncheck(self, locator):
        try:
            self.logger.info(f"uncheck the element with locator: {locator}")
            locator.uncheck()
        except Exception as error:
            self.logger.error(f"uncheck failed for {locator}: {error}")
            raise

    def select(self, locator, value):
        try:
            self.logger.info(f"select the {value} with locator: {locator}")
            locator.select_option(value)
        except Exception as error:
            self.logger.error(f"select {value} failed for {locator}: {error}")
            raise

    def get_text(self, locator):
        try:
            self.logger.info(f"get the text of elemnt with locator: {locator}")

            return locator.text_content()
        except Exception as error:
            self.logger.error(f"get text failed for {locator}: {error}")
            raise

    def is_visible(self, locator):
        try:
            self.logger.info(f"checking element vissible with locator: {locator}")
        
            return locator.is_visible()
        except Exception as error:
                    self.logger.error(f" visible failed for {locator}: {error}")
                    raise
         


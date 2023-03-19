from pages.basePage import BasePage
from config.locators import Locators

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def search_video(self, text, logger):
        self.wait_until_present_and_visible(Locators.search_bar)
        try:
            self.send_keys(Locators.search_bar, text)
            logger.info(f"Text:'{text} populated in the search bar.")
            self.click(Locators.search_btn)
        except:
            logger.exception(f"Text:'{text}' could not be populated in the search bar.")
from pages.basePage import BasePage
from config.locators import Locators

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def search_video(self, text, logger):
        self.wait_until_present_and_visible(Locators.search_bar)
        try:
            self.clear_inputField(Locators.search_bar)
            self.send_keys(Locators.search_bar, text)
            logger.info(f"Text:'{text}' populated in the search bar.")
            try:
                self.click(Locators.search_btn)
                self.wait_until_title_contains(text)
                logger.info("Search button clicked.")
            except:
                logger.error("Search button couldn't be clicked.")
                raise Exception()
        except:
            logger.exception(f"Text:'{text}' couldn't be searched.")
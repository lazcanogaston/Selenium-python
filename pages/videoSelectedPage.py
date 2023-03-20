from pages.basePage import BasePage
from config.locators import Locators
from pages.searchResultsPage import SearchResultsPage

class VideoSelectedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def validate_like_dislike_buttons(self, homePage_instance, iteration_name, iteration_values, logger):
        self.wait_until_title_contains("YouTube")
        homePage_instance.search_video(iteration_values['search_text'], logger)
        searchResultsPage = SearchResultsPage(self.driver)
        # The following dictionary contains the values of the result title locators for the two possible scenarios 1: user logged / 2: user not logged 
        results_locators = {
            "signed_in_user": f"({Locators.result_titles})[1]",
            "not_logged_user" : f"({Locators.result_titles_notLogged})[1]"
        }
        searchResultsPage.wait_until_present_and_visible(results_locators[iteration_name])
        searchResultsPage.find_element(results_locators[iteration_name]).click()
        searchResultsPage.wait_until_present_and_visible(Locators.like_btn)
        searchResultsPage.click(Locators.like_btn)
        logger.info("Like button pressed.")
        if "signed_in_user" in iteration_name:
            try:
                #check like functionality
                searchResultsPage.wait3_until_attribute_contains(Locators.like_btn, "aria-pressed", "true")
                logger.info("PASS: 'like' video correctly.")
                searchResultsPage.click(Locators.like_btn)
                searchResultsPage.wait3_until_attribute_contains(Locators.like_btn, "aria-pressed", "false")
                logger.info("PASS: 'like' removed correctly.")
                #check dislike functionality
                searchResultsPage.click(Locators.dislike_btn)
                searchResultsPage.wait3_until_attribute_contains(Locators.dislike_btn, "aria-pressed", "true")
                logger.info("PASS: 'dislike' video correctly.")
                searchResultsPage.click(Locators.dislike_btn)
                searchResultsPage.wait3_until_attribute_contains(Locators.dislike_btn, "aria-pressed", "false")
                logger.info("PASS: remove 'dislike' correctly.")
                #check cross status 
                searchResultsPage.click(Locators.like_btn)
                searchResultsPage.wait3_until_attribute_contains(Locators.like_btn, "aria-pressed", "true")
                searchResultsPage.wait3_until_attribute_contains(Locators.dislike_btn, "aria-pressed", "false")
                logger.info("PASS: 'like' video correctly.")
                searchResultsPage.click(Locators.dislike_btn)
                searchResultsPage.wait3_until_attribute_contains(Locators.dislike_btn, "aria-pressed", "true")
                searchResultsPage.wait3_until_attribute_contains(Locators.like_btn, "aria-pressed", "false")
                logger.info("PASS: 'like' removed and 'dislike' video correctly.")
                searchResultsPage.click(Locators.dislike_btn)
                logger.info("PASS: remove 'dislike' correctly.")
                logger.info("PASS-TEST: Like and dislike buttons functionality working as expected.")  
            except:
                logger.error("TEST-FAIL: Like and dislike buttons functionality is not working as expected.")
        elif "not_logged_user" in iteration_name:
            try:
                searchResultsPage.wait3_until_element_is_clickeable(Locators.accept_modal_btn)
                logger.info("PASS: Like modal displayed.")
            except:
                logger.error("FAIL: Like modal not displayed.")
            try:
                searchResultsPage.click(Locators.dislike_btn)
                searchResultsPage.wait3_until_element_is_clickeable(Locators.accept_modal_btn)
                logger.info("PASS: Dislike modal displayed.")
                logger.info("PASS-TEST: Like and dislike buttons functionality working as expected.")
            except:
                logger.error("TEST-FAIL: Dislike modal not displayed.")
            
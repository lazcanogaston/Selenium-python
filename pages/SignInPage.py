import time
from config.locators import Locators
from pages.basePage import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class SignInPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def sign_in(self, user, password, logger):
        self.get_url("https://www.youtube.com/")
        try:
            self.wait_until_visible(Locators.access_btn)
            logger.info("Sign In Page loaded correctly.")
        except:
            logger.error("Sign In Page can't be loaded.")
            raise Exception()
        try:
            self.click(Locators.access_btn)
            # self.wait_until_visible(Locators.use_other_account)
            # self.click(Locators.use_other_account)
            self.send_keys(Locators.signIn_user, user)
            self.click(Locators.signIn_next_btn)
            logger.info("User name populated correctly.")
            time.sleep(5)
            self.wait_until_present_and_visible(Locators.signIn_pass)
            self.send_keys(Locators.signIn_pass, password)
            logger.info("Password populated correctly.")
        
        except:
            logger.error("Username or password couldn't be populated.")
            raise Exception()
        try:
            self.click(Locators.signIn_next_btn)
            logger.info("Login button clicked correctly.")
            self.wait_until_url_to_be('https://www.youtube.com/')
            logger.info(f"PASS: User: {user} logged in successfully")
        except:
            logger.error(f"FAIL: User: {user} couldn't be logged in.")
            raise Exception()
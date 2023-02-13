import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from pages.googlePage import GooglePage
from utilities.logger import Logger
from config.locators import Locators
from selenium.webdriver.common.keys import Keys

class TestBasicSearch():

    @pytest.mark.parametrize("iteration_name, iteration_value", [("facebook_search", "facebook"), ("amazon search", "amazon")])
    def test_google_search(self, iteration_name, iteration_value, init_driver):
        driver = init_driver
        logger = Logger._init_logger_txt(iteration_name)
        logger.info(f'//////////// {iteration_name} Execution Started ////////////')
        try:
            try:
                driver.get("https://www.google.com")
                googlePage = GooglePage(driver)
                googlePage.wait_until_title_contains("Google")
                logger.info("The driver is in the desired URL.")
            except:
                logger.error("The driver couldn't get the desired URL.")
                raise Exception("The driver couldn't get the desired URL.")
            try:
                googlePage.send_keys(Locators.google_search_bar, iteration_value)
                googlePage.send_keys(Locators.google_search_bar, Keys.ENTER)
                googlePage.wait_until_title_contains(iteration_value)
                assert True
            except:
                logger.error(f"The search: {iteration_value} couldn't be reached.")
                raise Exception(f"The search: {iteration_value} couldn't be reached.")
        except:
            assert False
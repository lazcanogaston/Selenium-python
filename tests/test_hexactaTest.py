import json
import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from pages.googlePage import GooglePage
from pages.hexactaHomePage import HexactaHomePage
from utilities.logger import Logger
from config.locators import Locators
from selenium.webdriver.common.keys import Keys

class TestHexacta():
    
    #@pytest.mark.parametrize("iteration_name, iteration_value", [(1,1)])
    def test_hexacta(self, init_driver):
        driver = init_driver
        logger = Logger._init_logger_txt("test Hexacta")
        logger.info(f'//////////// {"test Hexacta"} Execution Started ////////////')
        try:
            driver.maximize_window()
            driver.get('https://www.hexacta.com/')
            homePage = HexactaHomePage(driver)
            homePage.wait_until_visible(Locators.home_page_search_btn)
            homePage.click(Locators.home_page_search_btn)
            homePage.wait_until_visible(Locators.search_input)
            homePage.send_keys(Locators.search_input, "Outsource")
            homePage.send_keys(Locators.search_input, Keys.ENTER)
            homePage.wait_until_title_contains("Outsource")
            
            if len(homePage.find_elements(Locators.articles.replace("replaceMe", "dsadassadasd"))) > 0:
                assert True
            else:
                assert False
            time.sleep(5)
        except:
            assert False
            

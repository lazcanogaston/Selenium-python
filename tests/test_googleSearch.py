import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from utilities.logger import Logger

class TestBasicSearch():

    @pytest.mark.parametrize("iteration_name, iteration_value", [("facebook_search", "facebook"), ("amazon search", "amazon")])
    def test_google_search(self, iteration_name, iteration_value, init_driver):
        driver = init_driver
        logger = Logger._init_logger_txt(iteration_name)
        logger.info(f'//////////// {iteration_name} Execution Started ////////////')
        driver.get("https://www.google.com")
        time.sleep(5)
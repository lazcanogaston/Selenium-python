import json
import os
import time
from dotenv import load_dotenv
import pytest
from config.locators import Locators
from pages.HomePage import HomePage
from pages.searchResultsPage import SearchResultsPage
from pages.videoSelectedPage import VideoSelectedPage
from tests.baseTest import BaseTest
from utilities.dsHandler import DsHandler
from utilities.logger import Logger
from pages.SignInPage import SignInPage

load_dotenv()

with open("C:\\Selenium-python\\config\\dataSets\\like_dislike dataSet.json", "r") as json_file:
    ds_dict = json.load(json_file) # converts json into dict


class TestLikeAndDislike(BaseTest):
    @pytest.mark.parametrize("iteration_name, iteration_values", DsHandler.read_dataset(ds_dict["testCase"]))
    def test_like_dislike_video(self, iteration_name, iteration_values, init_driver):
        driver = init_driver
        name = f"FRONTEND like functionality for {iteration_name}"
        logger = Logger._init_logger_txt(name)
        logger.info(f"{iteration_name} execution started.")
        if "signed_in_user" in iteration_name:
            signIn_Page = SignInPage(driver)
            signIn_Page.sign_in(eval(iteration_values['user']), eval(iteration_values['pass']), logger)
            homePage = HomePage(driver) 
        elif "not_logged_user" in iteration_name:
            homePage = HomePage(driver) 
            homePage.get_url("https://www.youtube.com/")
            try:
                logged = False
                #  statement will be executed complete just if the user is logged
                homePage.wait_3_until_present_and_visible(Locators.avatar_btn)
                logged = True
            except:
                #executed just if first iteration fails and the user is not logged
                logger.info("User not logged as expected.")
            if logged == True:
                logger.info("User Logged. Logging out process started.")
                homePage.click(Locators.avatar_btn)
                homePage.wait3_until_element_is_clickeable(Locators.log_out_btn)
                homePage.click(Locators.log_out_btn)
                logger.info("User logged out.")
            
        videoSelectedPage = VideoSelectedPage(driver)
        videoSelectedPage.validate_like_dislike_buttons(homePage, iteration_name, iteration_values, logger)

        time.sleep(2)
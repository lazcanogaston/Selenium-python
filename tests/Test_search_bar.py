import json
import os
import time

from dotenv import load_dotenv
import pytest
from config.locators import Locators
from pages.HomePage import HomePage
from pages.searchResultsPage import SearchResultsPage
from tests.baseTest import BaseTest
from utilities.dsHandler import DsHandler
from utilities.logger import Logger
from pages.SignInPage import SignInPage

load_dotenv()

with open("C:\\Selenium-python\\config\\dataSets\\searchBar dataSet.json", "r") as json_file:
    ds_dict = json.load(json_file) # converts json into dict

first_run = True

class TestSearchBar(BaseTest):
    @pytest.mark.parametrize("iteration_name, iteration_values", DsHandler.read_dataset(ds_dict["testCase"]))
    def test_searchBar(self, iteration_name, iteration_values, init_driver):
        global first_run
        driver = init_driver
        name = f"FRONTEND Search bar {iteration_name}."
        logger = Logger._init_logger_txt(name)
        logger.info(f"{iteration_name} execution started.")
        if first_run == True:
            signIn_Page = SignInPage(driver)
            signIn_Page.sign_in(os.getenv('user_email'), os.getenv('user_password'), logger)
            first_run = False 
        homePage = HomePage(driver) 
        homePage.wait_until_title_contains("YouTube")
        homePage.search_video(iteration_values['search_text'], logger)
        searchResultsPage = SearchResultsPage(driver)
        #METHOD BEFORE USING BASE TEST
        #fails = searchResultsPage.validate_searchBar_results(iteration_values['expected_result'], logger)
        #METHOS USING BASE TEST
        results = searchResultsPage.searchBar_results(iteration_values['search_text'], logger)
        if len(results) == 0:
            logger.error("The search results list is empty.")
        else:
            logger.info(f"The results list contains {len(results)} items.")
            logger.info(f"Results list: {results}.") # if this line is not in the logger is because of icons in the youtube description
        fails = BaseTest.validate_json_response(results, iteration_values['expected_result'])

        if fails > 0:
            logger.error(f"TEST FAILED IN {fails} VALIDATIONS: There results doesn't match with the search query.")
            assert False
        else:
            logger.info("TEST PASSED: All results matches the search query criteria.")


#EL OTRO TEST PUEDE SER DE LOGUEARSE, BUSCAR ALGO, GUARDAR EL PRIMER VIDEO EN VER MAS TARDE O DARLE LIKE, IR AL PERFIL, BUSCAR LOS QUE VIDEOS QUE ME GUSTAN Y FIJARME QUE ESTA EL QUE GUARDE, DESPUES AGARRAR Y SACARLE EL LIKE, ABRIR EL VIDEO Y VER QUE YA NO LO TENGA MAS
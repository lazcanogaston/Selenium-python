import json
import os
import time

from dotenv import load_dotenv
import pytest
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
    def test_aaa(self, iteration_name, iteration_values, init_driver):
        global first_run
        driver = init_driver
        logger = Logger._init_logger_txt(iteration_name)
        if first_run == True:
            signIn_Page = SignInPage(driver)
            signIn_Page.sign_in(os.getenv('user_email'), os.getenv('user_password'), logger)
            first_run = False
        homePage = HomePage(driver)
        homePage.search_video(iteration_values['search_text'], logger)
        #assert
        searchResultsPage = SearchResultsPage(driver)
        #METHOD BEFORE USING BASE TEST
        #fails = searchResultsPage.validate_searchBar_results(iteration_values['expected_result'], logger)
        #METHOS USING BASE TEST
        possible_results = searchResultsPage.searchBar_results(logger)
        fails = BaseTest.validate_json_response(possible_results, iteration_values['expected_result'])

        if fails > 0:
            logger.error(f"TEST FAILED IN {fails} VALIDATIONS: There results doesn't match with the search query.")
            assert False
        else:
            logger.info("TEST PASSED: All results matches the search query criteria.")
        time.sleep(10)


#EL OTRO TEST PUEDE SER DE LOGUEARSE, BUSCAR ALGO, GUARDAR EL PRIMER VIDEO EN VER MAS TARDE O DARLE LIKE, IR AL PERFIL, BUSCAR LOS QUE VIDEOS QUE ME GUSTAN Y FIJARME QUE ESTA EL QUE GUARDE, DESPUES AGARRAR Y SACARLE EL LIKE, ABRIR EL VIDEO Y VER QUE YA NO LO TENGA MAS
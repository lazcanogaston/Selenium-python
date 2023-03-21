import json
import pytest
import requests
import os
from dotenv import load_dotenv
from tests.baseTest import BaseTest
from utilities.dsHandler import DsHandler
from utilities.logger import Logger

load_dotenv()

with open("C:\\Selenium-python\\config\\dataSets\\backend_searchBar dataSet.json", "r") as json_file:
    ds_dict = json.load(json_file) # converts json into dict

class TestSearchBarBackend(BaseTest):
    #@pytest.mark.skip
    @pytest.mark.parametrize("iteration_name, iteration_values", DsHandler.read_dataset(ds_dict["testCase"]))
    def test_search_status_code(self, iteration_name, iteration_values):
        logger = Logger._init_logger_txt(iteration_name)
        
        base_url = 'https://www.googleapis.com/youtube/v3/search/'
        
        params = {
            "part": iteration_values['part_param'],
            "q": iteration_values["search_text"],  # search query
            "type": "video",
            "key": os.getenv('api_key') 
        }
        try:
            response = requests.get(base_url, params=params)
            body_response = json.loads(response.text)
            if "pass" in iteration_name and response.status_code == iteration_values["expected_status"]:
                logger.info(f"PASS-TEST: The status is 200 as expected.")
                assert True
                
            elif "fail" in iteration_name and response.status_code == iteration_values["expected_status"]:
                logger.info(f"PASS-TEST: The status is {response.status_code} as expected.")
                assert True
            else:
                logger.error(f"TEST-FAIL: The status is {response.status_code} and it should be {iteration_values['expected_status']}.")
                assert False
        except:
            logger.error("The request is invalid.")
            assert False

    #@pytest.mark.skip
    @pytest.mark.parametrize("iteration_name, iteration_values", DsHandler.read_dataset(ds_dict["testCase"]))
    def test_search_response(self, iteration_name, iteration_values):
        
        name = f"{iteration_name} search results "
        logger = Logger._init_logger_txt(name)

        base_url = 'https://www.googleapis.com/youtube/v3/search/'
        
        params = {
            "part": iteration_values['part_param'],
            "q": iteration_values["search_text"],  # search query
            "type": "video",
            "key": os.getenv('api_key') 
        }
        try:
            response = requests.get(base_url, params=params)
            body_response = json.loads(response.text)
            response_texts = list(map(lambda i: i['snippet']['title'].lower().replace(" ", ""), body_response['items']))
            logger.info(response_texts)
            fails = BaseTest.validate_json_response(response_texts, iteration_values['expected_result'])
            if "pass" in iteration_name: 
                if fails > 0:
                    logger.error(f"FAIL-TEST: There are {fails} fails in the response.")
                    assert False
                else: 
                    logger.info("PASS-TEST: The response matches the search criteria.")
        except AssertionError:
            logger.error("The request is valid but the response doesn't match the search criteria.")
            assert False
        except :
            if "fail" in iteration_name and response.status_code == iteration_values['expected_status']:
                logger.info(f"PASS-TEST: The request is invalid and the status code is {iteration_values['expected_status']} as expected.")
                assert True
            else:
                logger.error("The request is invalid.")
                assert False
        
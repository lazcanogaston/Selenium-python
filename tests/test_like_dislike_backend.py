import json
import pytest
import requests
import os
from dotenv import load_dotenv
from tests.baseTest import BaseTest
from utilities.dsHandler import DsHandler
from utilities.logger import Logger
from config.variables import Variables

load_dotenv()

with open("C:\\Selenium-python\\config\\dataSets\\backend_like_functionality dataSet.json", "r") as json_file:
    ds_dict = json.load(json_file) # converts json into dict

class TestLikeAndDislikeBackend(BaseTest):

    @pytest.mark.parametrize("iteration_name, iteration_values", DsHandler.read_dataset(ds_dict["testCase"]))
    def test_like_video(self, iteration_name, iteration_values):
        name = f"BACKEND {iteration_name}"
        logger = Logger._init_logger_txt(name)
        logger.info(f"{iteration_name} execution started.")
        endpoint = 'https://www.googleapis.com/youtube/v3/videos/rate'
        
        params = {"id": iteration_values['id_param'],
                  "rating": iteration_values['rating_param']}
        
        bearer_token= eval(iteration_values['bearer_token'])
        
        headers = {"Authorization": f"Bearer {bearer_token}"}
        
        response = requests.post(url = endpoint, params=params, headers=headers)
        logger.info(response.status_code)
        if response.status_code == iteration_values['expected_status']:
            logger.info(f"TEST-PASSED. Response status is {iteration_values['expected_status']} as expected.")
            assert True
        else:
            logger.error(f"TEST-FAIL: Response status is {response.status_code} and it should be: {iteration_values['expected_status']}.")
            assert False
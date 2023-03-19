import json
import requests
import os
from dotenv import load_dotenv
from utilities.logger import Logger

load_dotenv()
class TestBackend():
    
    def test_search(self):
        logger = Logger._init_logger_txt("test 2")
        
        base_url = 'https://www.googleapis.com/youtube/v3/search'
        
        params = {
            "part": "snippet",
            "q": "cat videos",  # search query
            "type": "video",
            "key": os.getenv('api_key') 
        }
        try:
            response = requests.get(base_url, params=params)
            if response.status_code == 200:
                logger.info("ENTRO")
                #items_list = response.json()['items']
                logger.info(response.status_code)
                logger.info(response.text)
                logger.info(response.json())
            else:
                logger.error("falla")
        except:
            logger.error("falla")
        
        
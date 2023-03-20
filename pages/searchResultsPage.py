import time
from config.locators import Locators
from pages.basePage import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class SearchResultsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    
    # def validate_searchBar_results(self, expected_result, logger):
    #     fails = 0
    #     self.wait_until_present_and_visible(f"({Locators.result_titles})[1]")
    #     # returns the list of the searche results
    #     results = self.find_elements(Locators.result_titles) 
    #     # get the aria-label attibute of each result and convert it to lower case
    #     results_content = list(map(lambda i: i.get_attribute("aria-label").lower(), results)) 
    #     logger.info(f"Results list: {results_content}.")
    #     possible_results = len(expected_result)
        
    #     fails = 0
    #     for result in results_content:
    #         it = 0
    #         assertion = False
    #         while it < possible_results:
    #             if expected_result[it] in result:
    #                 assertion = True
    #                 break
    #             it += 1
    #         if assertion == False:
    #             fails += 1  
    #     return fails
            
    def searchBar_results(self, search_text, logger):
        results_content = []
        self.wait_until_title_contains(search_text)
        self.wait_until_present_and_visible(f"({Locators.result_titles})[1]")
        #self.wait_until_visible(f"({Locators.result_titles})[1]")
        # returns the list of the searche results
        results = self.find_elements(Locators.result_titles) 
        # get the aria-label attibute of each result and convert it to lower case
        results_content = list(map(lambda i: i.get_attribute("aria-label").lower(), results)) 
        return results_content


        
        
        
        # for result in results_content:
        #     for expected in expected_result:
        #         if expected in result:
        #             break
        #         else:
        #             fails += 1
        # return fails
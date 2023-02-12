import pytest 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope= 'class')
def init_driver():
    # selenium 4 to execute tests locally if not, we need to instance the driver with the URL of the selenium hub 
    
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()
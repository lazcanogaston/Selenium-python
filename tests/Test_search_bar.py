import os
import time

from dotenv import load_dotenv
from pages.HomePage import HomePage
from utilities.logger import Logger
from pages.SignInPage import SignInPage

load_dotenv()
class TestSearchBar():

    def test_aaa(self, init_driver):
        driver = init_driver
        logger = Logger._init_logger_txt("test 2")
        signIn_Page = SignInPage(driver)
        signIn_Page.sign_in(os.getenv('user_email'), os.getenv('user_password'), logger)
        homePage = HomePage(driver)
        #time.sleep(5)
        homePage.search_video("cats", logger)
        time.sleep(10)


#EL OTRO TEST PUEDE SER DE LOGUEARSE, BUSCAR ALGO, GUARDAR EL PRIMER VIDEO EN VER MAS TARDE O DARLE LIKE, IR AL PERFIL, BUSCAR LOS QUE VIDEOS QUE ME GUSTAN Y FIJARME QUE ESTA EL QUE GUARDE, DESPUES AGARRAR Y SACARLE EL LIKE, ABRIR EL VIDEO Y VER QUE YA NO LO TENGA MAS
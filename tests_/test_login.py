##step3:
# from pages.login_page import LoginPage
# def test_login_page():
#     loginpage = LoginPage()
#     loginpage.click_on_login_link()
#     loginpage.enter_email()
#     loginpage.enter_password()
#     loginpage.click_on_remember_me()
#     loginpage.click_on_login_btn()


####step4:
# from pages.login_page import LoginPage
# from selenium import webdriver
# opt=webdriver.ChromeOptions()
# opt.add_experimental_option('detach',True)
# driver=webdriver.Chrome(options=opt)
# driver.maximize_window()
# driver.get('https://demowebshop.tricentis.com/')
#
# def test_login_page():
#     loginpage = LoginPage()
#     loginpage.click_on_login_link()
#     loginpage.enter_email()
#     loginpage.enter_password()
#     loginpage.click_on_remember_me()
#     loginpage.click_on_login_btn()


###########stpe5

# from pages.login_page import LoginPage
# from selenium import webdriver
# opt=webdriver.ChromeOptions()
# opt.add_experimental_option('detach',True)
# driver=webdriver.Chrome(options=opt)
# driver.maximize_window()
# driver.get('https://demowebshop.tricentis.com/')
#
# def test_login_page():
#     loginpage = LoginPage(driver)
#     loginpage.click_on_login_link()
#     loginpage.enter_email()
#     loginpage.enter_password()
#     loginpage.click_on_remember_me()
#     loginpage.click_on_login_btn()

#############################################################################
# step6:
# from pages.login_page import LoginPage
# import pytest
# from selenium import webdriver
# @pytest.fixture
# def browser_setup():
#     opt = webdriver.ChromeOptions()
#     opt.add_experimental_option('detach', True)
#     driver = webdriver.Chrome(options=opt)
#     driver.maximize_window()
#     driver.get('https://demowebshop.tricentis.com/')
#     yield driver
#     driver.quit()
#
# def test_login_page(browser_setup):
#     loginpage = LoginPage(browser_setup)
#     loginpage.click_on_login_link()
#     loginpage.enter_email()
#     loginpage.enter_password()
#     loginpage.click_on_remember_me()
#     loginpage.click_on_login_btn()
###############################################################3
# step7:
# from pages.login_page import LoginPage
# def test_login_page(browser_setup):
#     loginpage = LoginPage(browser_setup)
#     loginpage.click_on_login_link()
#     loginpage.enter_email()
#     loginpage.enter_password()
#     loginpage.click_on_remember_me()
#     loginpage.click_on_login_btn()

####################################################################
# ##step9:
# from pages.login_page import LoginPage
# def test_login_page(browser_setup):
#     loginpage = LoginPage(browser_setup)
#     loginpage.login()

#######################################################################
# #step10:
import pytest
from utilities.data_extraction import get_login_cred
from pages.login_page import LoginPage

@pytest.mark.parametrize('username,password',get_login_cred())
def test_login_page(browser_setup,username,password):
    loginpage = LoginPage(browser_setup)
    loginpage.login(username,password)
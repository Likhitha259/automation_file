# ###step1
# from selenium import webdriver
# opt=webdriver.ChromeOptions()
# opt.add_experimental_option('detach',True)
# driver=webdriver.Chrome(options=opt)
# driver.maximize_window()
# driver.get('https://demowebshop.tricentis.com/')
# driver.find_element('xpath',"//a[.='Log in']").click()
# driver.find_element('id','Email').send_keys('krishnavasu25@gmail.com')
# driver.find_element('id','Password').send_keys('Krishna@25')
# driver.find_element('css selector','input[name="RememberMe"]').click()
# driver.find_element('css selector','input[value="Log in"]').click()

####step2
# creating the class and all the action is been converted to method
# from selenium import webdriver
# opt=webdriver.ChromeOptions()
# opt.add_experimental_option('detach',True)
# driver=webdriver.Chrome(options=opt)
# driver.maximize_window()
# driver.get('https://demowebshop.tricentis.com/')
# class LoginPage:
#     def click_on_login_link(self):
#         driver.find_element('xpath', "//a[.='Log in']").click()
#
#     def enter_email(self):
#         driver.find_element('id', 'Email').send_keys('krishnavasu25@gmail.com')
#
#     def enter_password(self):
#         driver.find_element('id', 'Password').send_keys('Krishna@25')
#
#     def click_on_remember_me(self):
#         driver.find_element('css selector', 'input[name="RememberMe"]').click()
#
#     def click_on_login_btn(self):
#         driver.find_element('css selector', 'input[value="Log in"]').click()

# loginpage=LoginPage()
# loginpage.click_on_login_link()
# loginpage.enter_email()
# loginpage.enter_password()
# loginpage.click_on_remember_me()
# loginpage.click_on_login_btn()


#####################################################################################################
##step3:
##moving the object creation to the test file
# from selenium import webdriver
# opt=webdriver.ChromeOptions()
# # opt.add_experimental_option('detach',True)
# driver=webdriver.Chrome(options=opt)
# driver.maximize_window()
# driver.get('https://demowebshop.tricentis.com/')
# class LoginPage:
#     def click_on_login_link(self):
#         driver.find_element('xpath', "//a[.='Log in']").click()
#
#     def enter_email(self):
#         driver.find_element('id', 'Email').send_keys('krishnavasu25@gmail.com')
#
#     def enter_password(self):
#         driver.find_element('id', 'Password').send_keys('Krishna@25')
#
#     def click_on_remember_me(self):
#         driver.find_element('css selector', 'input[name="RememberMe"]').click()
#
#     def click_on_login_btn(self):
#         driver.find_element('css selector', 'input[value="Log in"]').click()

# ###step4:moving the driver method[setup] into the test file

# class LoginPage:
#     def click_on_login_link(self):
#         driver.find_element('xpath', "//a[.='Log in']").click()
#
#     def enter_email(self):
#         driver.find_element('id', 'Email').send_keys('krishnavasu25@gmail.com')
#
#     def enter_password(self):
#         driver.find_element('id', 'Password').send_keys('Krishna@25')
#
#     def click_on_remember_me(self):
#         driver.find_element('css selector', 'input[name="RememberMe"]').click()
#
#     def click_on_login_btn(self):
#         driver.find_element('css selector', 'input[value="Log in"]').click()

##error:as the driver is not present
#########################################################################

###step5:created constructor and passed driver as the object property from test file

# class LoginPage:
#     def __init__(self,driver):
#         self.driver=driver
#
#     def click_on_login_link(self):
#         login=self.driver.find_element('xpath', "//a[.='Log in']")
#         login.click()
#
#     def enter_email(self):
#         email=self.driver.find_element('id', 'Email')
#         email.clear()
#         email.send_keys('krishnavasu25@gmail.com')
#
#     def enter_password(self):
#         self.driver.find_element('id', 'Password').send_keys('Krishna@25')
#
#     def click_on_remember_me(self):
#         self.driver.find_element('css selector', 'input[name="RememberMe"]').click()
#
#     def click_on_login_btn(self):
#         self.driver.find_element('css selector', 'input[value="Log in"]').click()
#
############################################################################
#step8:converting the locators into the form of class member and unpacking the same in the methods


# class LoginPage:
#     login_link=('xpath', "//a[.='Log in']")
#     email_loc=('id', 'Email')
#     pass_loc=('id', 'Password')
#     remeber_loc=('css selector', 'input[name="RememberMe"]')
#     login_btn=('css selector', 'input[value="Log in"]')
#
#     def __init__(self,driver):
#         self.driver=driver
#
#     def click_on_login_link(self):
#         login=self.driver.find_element(*self.login_link)
#         login.click()
#
#     def enter_email(self):
#         email=self.driver.find_element(*self.email_loc)
#         email.clear()
#         email.send_keys('krishnavasu25@gmail.com')
#
#     def enter_password(self):
#         self.driver.find_element(*self.pass_loc).send_keys('Krishna@25')
#
#     def click_on_remember_me(self):
#         self.driver.find_element(*self.remeber_loc).click()
#
#     def click_on_login_btn(self):
#         self.driver.find_element(*self.login_btn).click()

##########################################################################

## step9:
# from pages.base_page import BasePage
# class LoginPage(BasePage):
#     login_link = ('xpath', "//a[.='Log in']")
#     email_loc = ('id', 'Email')
#     pass_loc = ('id', 'Password')
#     remeber_loc = ('css selector', 'input[name="RememberMe"]')
#     login_btn = ('css selector', 'input[value="Log in"]')
#     def __init__(self,driver):
#         super().__init__(driver)
#     def login(self):
#         self.click(self.login_link)
#         self.send_keys(self.email_loc,'krishnavasu25@gmail.com')
#         self.send_keys(self.pass_loc,'Krishna@25')
#         self.click(self.remeber_loc)
#         self.click(self.login_btn)

###########################################################################
# #step 10:
from pages.base_page import BasePage
class LoginPage(BasePage):
    login_link = ('xpath', "//a[.='Log in']")
    email_loc = ('id', 'Email')
    pass_loc = ('id', 'Password')
    remeber_loc = ('css selector', 'input[name="RememberMe"]')
    login_btn = ('css selector', 'input[value="Log in"]')
    def __init__(self,driver):
        super().__init__(driver)
    def login(self,username,password):
        self.click(self.login_link)
        self.send_keys(self.email_loc,username)
        self.send_keys(self.pass_loc,password)
        self.click(self.remeber_loc)
        self.click(self.login_btn)

    print('from dummy')
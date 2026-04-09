class BasePage:
    def __init__(self,driver):
        self.driver=driver

    def send_keys(self,locator,text):
        '''this methods takes locator and text'''
        ele1=self.driver.find_element(*locator)  #*locator=loc_name,loc_value
        ele1.clear()
        ele1.send_keys(text)

    def click(self,locator):
        ele2=self.driver.find_element(*locator)
        ele2.click()

    print('hai hello')
    print('this is from dummy branch')
print('this is coming from dummy')
print('this is coming from duplicate')
import time,allure
from selenium.webdriver.support.wait import WebDriverWait


class Base_Method:
    def __init__(self,driver):
        self.driver = driver
    def find_element(self,loc,timeout=15,poll=1):
        return WebDriverWait(self.driver,timeout,poll).until(lambda x:x.find_element(*loc))
    def find_elements(self,loc,timeout=15,poll=1):
        return WebDriverWait(self.driver,timeout,poll).until(lambda x:x.find_elements(*loc))
    def click_element(self,loc):
        self.find_element(loc).click()
    @allure.step(title='输入操作')
    def send_keys_text(self,loc,text,input_name):
        element = self.find_element(loc)
        element.clear()
        allure.attach('input_name','{0}'.format(input_name))
        element.send_keys(text)
    def gain_screenshot(self):
        self.time = time.strftime('%Y-%m-%d_%H-%M-%S',time.localtime(time.time()))
        return self.driver.get_screenshot_as_file\
            ('C:/Users/Administrator/PycharmProjects/App_1213/Gain_Screenshot/app_%s.png'% self.time)
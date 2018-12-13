from appium import webdriver


class Get_Driver:
    def get_driver(self,appPackage,appActivity):
        self.desired = {}
        self.desired['platformName'] = 'Android'
        self.desired['platformVersion'] = '8.0.0'
        self.desired['deviceName'] = 'HUAWEI nova2'
        self.desired['appPackage'] = appPackage
        self.desired['appActivity'] = appActivity
        self.desired['unicodeKeyboard'] = True
        self.desired['resetKeyboard'] = True
        return webdriver.Remote('http://localhost:4723/wd/hub',self.desired)
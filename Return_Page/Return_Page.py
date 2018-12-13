from Page.Opearting_Method import Opearting_Method

class Return_Page:
    def __init__(self,driver):
        self.driver = driver
    def return_page(self):
        return Opearting_Method(self.driver)
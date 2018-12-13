from Base.Base_Method import Base_Method
import Page,allure
class Opearting_Method(Base_Method):
    def __init__(self,driver):
        Base_Method.__init__(self,driver)
    # 点击回退按钮
    @allure.step(title='点击回退按钮')
    def click_back_button(self):
        self.click_element(Page.back_button)
    # 获取元素text列表
    def gain_text_list(self,element):
        self.text_list = []
        for i in self.find_elements(element):
            self.text_list.append(i.text)
        return self.text_list

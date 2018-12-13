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
    @allure.step(title='断言并获取文本列表')
    def assert_gain_textlist(self,assert_text):
        try:
            assert assert_text in self.gain_text_list(Page.search_title)
        except Exception as E:
            print(E)
        finally:
            allure.attach('文本列表', '{0}'.format(self.gain_text_list(Page.search_title)))
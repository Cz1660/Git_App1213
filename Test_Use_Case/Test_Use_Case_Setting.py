from Base.Get_Driver import Get_Driver
from Return_Page.Return_Page import Return_Page
from Yaml.Read_Yaml import Read_Yaml
import Page,time,pytest,allure

def gain_input_yaml():
    input_list = []
    yaml_data = Read_Yaml('Input_Yaml.yaml').read_yaml()
    for i in yaml_data.keys():
        input_list.append((i,yaml_data.get(i).get('input_text'),yaml_data.get(i).get('assert_text'),
                           yaml_data.get(i).get('text')))
    return input_list

class Test_Login:
    def setup_class(self):
        self.Dv = Return_Page(Get_Driver().get_driver('com.android.settings','.HWSettings'))
    def teardown_class(self):
        self.Dv.driver.quit()
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize('test_number,input_text,assert_text,text',gain_input_yaml())
    @allure.step(title='验证搜索功能的正确性' )
    def test_setting(self,test_number,input_text,assert_text,text):
        allure.attach('用例编号','{0}'.format(test_number))
        self.Dv.return_page().send_keys_text(Page.search_setting,input_text,input_text)
        time.sleep(1)
        @allure.step(title='抛异常，断言')
        def test_assert_setting():
            try:
                allure.attach('，获取的search_title', '{0}'.format(self.Dv.return_page().gain_text_list(Page.search_title)))
                assert assert_text in self.Dv.return_page().gain_text_list(Page.search_title)
            except Exception as E:
                print(E)
            finally:
                def test_finally():
                    print(test_number)
                    print(self.Dv.return_page().gain_text_list(Page.search_title))
                    self.Dv.return_page().click_back_button()
                test_finally()
        test_assert_setting()




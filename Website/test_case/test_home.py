import unittest
import function
import myunit
from Website.page_object.LoginPage import LoginPage
from Website.page_object.HomePage import HomePage
from time import sleep


class LoginTest(myunit.StartEnd):
    csv_file = '../data/account.csv'

    # @unittest.skip('skip this case')
    def test_home_normal(self):
        '''点击登录>点击电脑办公 正常1'''
        print("test_login1_normal is start test...===========")
        # po = LoginPage(self.driver)
        po = HomePage(self.driver)
        data = function.get_csv_data(self.csv_file, 1)
        print(data[0], data[1])
        # 登录>提交
        po.Login_action(data[0], data[1])
        po.type_submit()
        # 点击电脑办公
        po.Computer_office()

        sleep(5)
        print(po.type_loginPass_hint())
        self.assertEqual(po.type_loginPass_hint(), '帮助中心')
        # # po.isElementExist(po.type_loginPass_hint())
        # # self.driver.execute_script('window.scrollBy(0,1000)')
        # self.driver.execute_script('document.documentElement.scrollTop=1000')
        # self.driver.implicitly_wait(10)
        # function.insert_img(self.driver, "51zxw_login1_normal.png")
        # print("test_login1_normal test end!")

    @unittest.skip('skip this case')
    def test_login2_PasswdError(self):
        '''username is ok,passwd is error'''
        print("test_login2_passwdError is start test...")
        po = LoginPage(self.driver)
        po.Login_action('51zxw', 3333)
        sleep(2)

        self.assertEqual(po.type_loginFail_hint(), '')
        function.insert_img(self.driver, "test_login2_PasswdError.jpg")

    @unittest.skip('skip this case')
    def test_login3_empty(self):
        '''username and passwd is empty'''
        print("test_login3_empty is start test...")
        po = LoginPage(self.driver)
        po.Login_action('11', '1')
        po.type_submit()
        sleep(5)
        po.isElementExist(po.type_loginFail_hint())

        sleep(5)

        # self.assertEqual(po.type_loginFail_hint(),'')

        function.insert_img(self.driver, 'test_login3_empty.png')
        print("test_login3_empty test end")


if __name__ == '__main__':
    unittest.main()

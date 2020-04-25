import driver
from Website.page_object.BasePage import Page
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, ElementNotVisibleException, NoSuchElementException
from time import sleep, time


class LoginPage(Page):
    url = '/'

    username_loc = (By.ID, 'loginStr')
    password_loc = (By.ID, 'pwd')
    submit_loc = (By.XPATH, "//div/button[@class='btn radius size-L btn-danger']")

    def type_submit(self):
        self.find_element(*self.submit_loc).click()

    def type_username(self, username):
        self.find_element(*self.username_loc).send_keys(username)

    def type_password(self, password):
        self.find_element(*self.password_loc).send_keys(password)

    def Login_action(self,username, password):
        self.open()
        self.type_username(username)
        self.type_password(password)
        self.type_submit()
        # self.find_element(*self.username_loc).send_keys(username)
        # sleep(2)
        # self.find_element(*self.password_loc).send_keys(pwd)
        # sleep(2)

    loginPass_loc = (By.LINK_TEXT, '帮助中心')
    loginFail_loc = (By.XPATH, '//*[@id="loginFrom"]/div/div[7]/div')

    def type_loginPass_hint(self) -> object:
        return self.find_element(*self.loginPass_loc).text

    def type_loginFail_hint(self):
        return self.find_element(*self.loginFail_loc)

    def isElementExist(self, element):
        flag = True
        driver = self.driver
        try:
            driver.find_element_by_xpath(element)


        except:
            flag = False
            return flag

    def xh(self):
        t = True
        time.sleep(1)
        while t:
            driver.execute_script("window.scrollBy(0,1000)")
            try:
                driver.find_element('link_text', '没有更多推荐了，返回首页').click()
                time.sleep(1)
                t = False
            except:
                self.xh()

    def scrollBy_down(self, *loc):
        #  scrollBy(x,y)中，x为必须参数，表示向右滚动的像素值；
        # y也为必须参数，表示向下滚动的像素值
        return self.driver.execute_script('window.scrollBy(*loc)')

    # def scrollTo_up(self, *loc):
    #     # scrollTo(x,y) 中，x为必须参数，表示要在窗口文档显示区左上角显示的文档的x坐标；
    #     # y也为必须参数，表示要在窗口文档显示区左上角显示的文档的y坐标
    #     self.driver.execute_script('window.scrollTo(*loc)')
    #
    # def scrollTo_dom(self, *loc):
    #     # 10000表示一下拉到底
    #     self.driver.execute_script('document.documentElement.scrollTop=10000')

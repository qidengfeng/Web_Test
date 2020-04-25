import driver
from Website.page_object.BasePage import Page
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, ElementNotVisibleException, NoSuchElementException
from time import sleep, time
from Website.page_object.LoginPage import LoginPage


class HomePage(LoginPage):
    url = '/'

    office_loc = (By.CSS_SELECTOR, 'body>div.nav>div>a:nth-child(1)')
    password_loc = (By.ID, 'pwd')
    submit_loc = (By.XPATH, "//div/button[@class='btn radius size-L btn-danger']")


    # 首页：点击电脑办公
    def Computer_office(self):
        self.find_element(*self.office_loc).click()

    def type_loginPass_hint(self) -> object:
        return self.find_element(*self.loginPass_loc).text


    # 进入电脑办公》点击 计算机基础知识教程
    def Computer_Basis(self):
        pass





















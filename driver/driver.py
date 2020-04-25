#!/usr/local/bin/python3
from selenium import webdriver


# from selenium.webdriver.chrome.options import Options


def browser():
    # 这个是一个用来控制chrome以无界面模式打开的浏览器
    # 创建一个参数对象，用来控制chrome以无界面的方式打开
    # chrome_options = Options()
    # 后面的两个是固定写法 必须这么写
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--disable-gpu')
    # driver = webdriver.Chrome(r'/Users/dengfengqi/Library/Python/3.7/lib/python/site-packages/selenium/webdriver'
    #                           '/chromedriver', options=chrome_options)
    driver = webdriver.Chrome('/Users/dengfengqi/Library/Python/3.7/lib/python/site-packages/selenium/webdriver'
                              '/chromedriver')
    # driver=webdriver.Firefox()
    # driver = webdriver.Chrome()
    # # driver=webdriver.Ie()
    # # driver = webdriver.PhantomJS()
    #
    # driver.get("http://www.baidu.com")
    # print(driver.get_cookies())

    return driver


# if __name__ == '__main__':
#     browser()

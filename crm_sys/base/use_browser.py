#import time
from selenium import webdriver

class UseBrowser:

    driver = None

    def __init__(self):
        # options = webdriver.ChromeOptions()
        # options.add_argument('--headless')
        # self.driver = webdriver.Chrome(executable_path='../../base/chromedriver.exe',chrome_options=options)
        self.driver = webdriver.Chrome(executable_path='../../base/chromedriver.exe')
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
        UseBrowser.driver = self.driver
    @classmethod
    def quit(cls):
        UseBrowser.driver.quit()
# if __name__ == '__main__':
#     use = UseBrowser()
#     time.sleep(2)
#     UseBrowser.quit()

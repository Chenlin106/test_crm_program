import time

#from selenium import webdriver
class BrowserOperation:
    def __init__(self,driver):
        self.driver = driver
        #self.driver = webdriver.Chrome()
    def open_url(self,url):
        try:
            self.driver.get(url)
        except Exception as e:
            print('异常:',e)

    def send_keys(self,xpath,content):
        try:
            self.driver.find_element_by_xpath(xpath).clear()
            self.driver.find_element_by_xpath(xpath).send_keys(content)
        except Exception as e:
            print(e,'element not find')
    def click_element(self,xpath):
        try:
            click = self.driver.find_element_by_xpath(xpath)
            time.sleep(1)
            click.click()
        except Exception as e:
            print(e,'element not find')
    def get_text(self,xpath):
        try:
            text=self.driver.find_element_by_xpath(xpath).text
        except Exception as e:
            print(e)
            return None
        else:
            return text
    def get_alert(self):
        try:
            alert=self.driver.switch_to.alert.text
            self.driver.switch_to.alert.accept()
        except Exception as e:
            print(e)
            return None
        else:
            return alert
    def get_title(self):
        try:
            title=self.driver.title
        except Exception as e:
            print(e)
            return None
        else:
            return title
    def change_frame(self,framename):
        try:
            if '/' not in framename:
                self.driver.switch_to.parent_frame()
                self.driver.switch_to.frame(framename)
            else:
                self.driver.switch_to.parent_frame()
                self.driver.switch_to.frame(self.driver.find_element_by_xpath(framename))
        except Exception as e:
            print(e)
    def change_windows(self,window):
        for win in self.driver.window_handles:
            self.driver.switch_to.window(win)
            if self.driver.title == window:
                break
    def delete_readonly(self,id):
        self.driver.execute_script("document.getElementById('{}').readOnly=false".format(id))

# if __name__ == '__main__':
#     ub = UseBrowser()
#     bo = BrowserOperation(UseBrowser.driver)
#     bo.open_url('http://172.17.4.234:8080/crm/')
#     bo.send_keys('//*[@name="userNum"]','admin')
#     bo.send_keys('//*[@name="userPw"]','123456')
#     bo.click_element('//*[@id="in1"]')
#     UseBrowser.quit()
from t2020_10_27.crm_sys.util.crm_log import Crm_log
from t2020_10_27.crm_sys.util.yaml_opreation import YamlOperation

from t2020_10_27.crm_sys.base.browser_operation import BrowserOperation
from t2020_10_27.crm_sys.base.use_browser import UseBrowser


class Login:
    def __init__(self,url):
        ub = UseBrowser()
        self.bo = BrowserOperation(UseBrowser.driver)
        self.bo.open_url(url)
        self.yaml=YamlOperation('../../config/locator.yaml')
        self.log = Crm_log()
    def login_func(self,uname,pwd):
        self.log.set_message('-' * 5 + '登录功能开始','info')
        self.bo.send_keys(self.yaml.get_locator('LoginPage','username'),uname)
        self.log.set_message('-' * 5 + '输入用户名：' + uname,'info')
        self.bo.send_keys(self.yaml.get_locator('LoginPage','password'),pwd)
        self.log.set_message('-' * 5 + '输入密码：' + pwd, 'info')
        self.bo.click_element(self.yaml.get_locator('LoginPage','submit_button'))
        self.log.set_message('-' * 5 + '点击登录', 'info')



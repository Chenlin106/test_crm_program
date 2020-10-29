from crm_sys.util.crm_log import Crm_log
from crm_sys.util.dbperation import MysqlConnection
from crm_sys.util.yaml_opreation import YamlOperation
from crm_sys.web_page.loginpage.login_page import Login


class CustomerPage:
    def __init__(self, url, uname, pwd):
        self.login = Login(url)
        self.login.login_func(uname, pwd)
        self.yaml = YamlOperation('../../config/locator.yaml')
        self.log = Crm_log()
        self.bo = self.login.bo
        self.mc = MysqlConnection()
    def select_customer_message(self):
        self.log.set_message('change frame', 'info')
        self.bo.change_frame(self.yaml.get_locator('SelectCustomer', 'leftFrame'))
        self.log.set_message('click button:客户信息', 'info')
        self.bo.click_element(self.yaml.get_locator('SelectCustomer', 'customer_message'))
        self.log.set_message('select_customer_message finish', 'info')
    def select_customer_distribution(self):
        self.log.set_message('change frame', 'info')
        self.bo.change_frame(self.yaml.get_locator('SelectCustomer', 'leftFrame'))
        self.log.set_message('click button:客户分配', 'info')
        self.bo.click_element(self.yaml.get_locator('SelectCustomer', 'customer_distribution'))
        self.log.set_message('select_customer_distribution finish', 'info')
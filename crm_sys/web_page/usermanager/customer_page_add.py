from t2020_10_26.crm_sys.web_page.usermanager.customer_page import CustomerPage
import  re

class CustomerPageAdd(CustomerPage):
    def create_customer(self,**kwargs):
        self.select_customer_message()
        self.log.set_message('change frame', 'info')
        self.bo.change_frame(self.yaml.get_locator('CreateCustomer','mainframe'))
        self.log.set_message('click element', 'info')
        self.bo.click_element(self.yaml.get_locator('CreateCustomer','add_button'))
        self.log.set_message('input customer_name:' + kwargs.get('customer_name',''), 'info')
        self.bo.send_keys(self.yaml.get_locator('CreateCustomer','customer_name'),kwargs.get('customer_name',''))
        self.log.set_message('input customer_email:' + kwargs.get('cus_email',''), 'info')
        self.bo.send_keys(self.yaml.get_locator('CreateCustomer','customer_email'),kwargs.get('cus_email',''))
        self.log.set_message('change readOnly', 'info')
        self.bo.delete_readonly(self.yaml.get_locator('CreateCustomer','close_readonly'))
        self.log.set_message('input custome_birthday:' + kwargs.get('cus_bir',''), 'info')
        self.bo.send_keys(self.yaml.get_locator('CreateCustomer','customer_birthday'),kwargs.get('cus_bir',''))
        self.log.set_message('input option_manager:' + kwargs.get('create_manager',''), 'info')
        self.bo.send_keys(self.yaml.get_locator('CreateCustomer','create_manager'),kwargs.get('create_manager',''))
        self.log.set_message('click element', 'info')
        self.bo.click_element(self.yaml.get_locator('CreateCustomer','sure_button'))
        self.log.set_message('create_customer finish', 'info')
        alert = self.bo.get_alert()
        if alert == kwargs.get('alert'):
            self.select_customer_distribution()
            self.log.set_message('change frame', 'info')
            self.bo.change_frame(self.yaml.get_locator('DistributionCustomer', 'mainframe'))
            self.log.set_message('获得记录条数', 'info')
            text = self.bo.get_text('/html/body/form/table/tbody/tr[3]/td/table/tbody/tr/td[2]/table/tbody/tr/td[1]')
            num = re.findall('(\d\d+)',text)[0]
            self.log.set_message('解析获得记录条数：{}'.format(num), 'info')
            xpath_get = self.yaml.get_locator('DistributionCustomer','customer_message').format(num)
            get_message = self.bo.get_text(xpath_get)
            self.log.set_message('获得页面数据内容：{}'.format(get_message), 'info')
            self.mc.delete_message(self.yaml.get_locator('DistributionCustomer', 'delete_table_name'),self.yaml.get_locator('DistributionCustomer', 'delete_rules').format(kwargs.get('customer_name')))
            self.log.set_message('从数据库中删除新增的记录：{}'.format(get_message), 'info')
            if  get_message == kwargs.get('customer_name'):
                return True
        return False
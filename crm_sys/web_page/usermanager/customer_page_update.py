from t2020_10_26.crm_sys.web_page.usermanager.customer_page import CustomerPage

class CustomerPageUpdate(CustomerPage):
    def update_customer_message(self,**kwargs):
        self.select_customer_message()
        self.log.set_message('change frame', 'info')
        self.bo.change_frame(self.yaml.get_locator('UpdateCustomer','mainframe'))
        self.log.set_message('click update', 'info')
        self.bo.send_keys(self.yaml.get_locator('UpdateCustomer','select_customer'),kwargs.get('name',''))
        self.bo.click_element(self.yaml.get_locator('UpdateCustomer','select_customer_submit'))
        self.bo.click_element(self.yaml.get_locator('UpdateCustomer','update_button'))
        if kwargs.get('mobilephone') != None:
            self.bo.send_keys(self.yaml.get_locator('UpdateCustomer','mobilephone'), kwargs.get('mobilephone', ''))
        if kwargs.get('email') != None:
            self.bo.send_keys(self.yaml.get_locator('UpdateCustomer','email'), kwargs.get('email', ''))
        if kwargs.get('customerjob') !=None:
            self.bo.send_keys(self.yaml.get_locator('UpdateCustomer','customerjob'),kwargs.get('customerjob'))
        if kwargs.get('updatemanager') != None:
            self.bo.send_keys(self.yaml.get_locator('UpdateCustomer','updatemanager'), kwargs.get('updatemanager', ''))
        self.bo.click_element(self.yaml.get_locator('UpdateCustomer','submit_button'))
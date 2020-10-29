import time
import unittest
from HTMLTestRunner import HTMLTestRunner

import sys
sys.path.append('G:\\PYtest\\day1')
from t2020_10_27.crm_sys.util.excel_operation import OperationExcel
from t2020_10_27.crm_sys.web_page.usermanager.customer_page_update import CustomerPageUpdate
from t2020_10_27.crm_sys.base.use_browser import UseBrowser




class TestUpdateCustomer(unittest.TestCase):
    def setUp(self) -> None:
        self.op = OperationExcel('../../config/test_case.xlsx', '修改客户用例参数')
        self.customerupdate = CustomerPageUpdate(self.op.get_cell(1,1),self.op.get_cell(1,2),self.op.get_cell(1,3))
        self.bo = self.customerupdate.bo
    def tearDown(self) -> None:
        UseBrowser.quit()
    def test_update_customer_message(self):
        name = self.op.get_cell(1,4)
        customerjob=self.op.get_cell(1,5)
        self.customerupdate.update_customer_message(name=name,customerjob=customerjob)
        alert = self.bo.get_alert()
        self.assertEqual(alert,self.op.get_cell(1,6))
if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    testcase = unittest.TestLoader().loadTestsFromTestCase(TestUpdateCustomer)
    suite.addTests(testcase)
    date_now = time.strftime('%Y-%m-%d', time.localtime())
    with open('../../report/UpdateCustomer_test_report_.html', 'wb+') as file:
    #with open('../../report/UpdateCustomer_test_report_' + date_now + '_.html', 'wb+') as file:
        runner = HTMLTestRunner(stream=file, verbosity=2, title='Login_auto_test', description='ui_test')
        runner.run(suite)

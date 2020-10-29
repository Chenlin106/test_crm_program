import time
import unittest
from HTMLTestRunner import HTMLTestRunner

import sys
sys.path.append('G:\\PYtest\\day1')
from t2020_10_27.crm_sys.util.excel_operation import OperationExcel
from t2020_10_27.crm_sys.web_page.usermanager.customer_page_add import CustomerPageAdd
from t2020_10_27.crm_sys.base.use_browser import UseBrowser




class TestAddCustomer(unittest.TestCase):
    def setUp(self) -> None:
        self.op = OperationExcel('../../config/test_case.xlsx', '添加客户用例参数')
        self.customeradd = CustomerPageAdd(self.op.get_cell(1,1),self.op.get_cell(1,2),self.op.get_cell(1,3))
        self.bo = self.customeradd.bo
    def tearDown(self) -> None:
        UseBrowser.quit()
    def test_create_customer_success(self):
        customer_name = self.op.get_cell(1,4)
        cus_email = self.op.get_cell(1,5)
        cus_bir = self.op.get_cell(1,6)
        create_manager = self.op.get_cell(1,7)
        alert = self.op.get_cell(1,8)
        get=self.customeradd.create_customer(customer_name=customer_name,cus_email=cus_email,cus_bir=cus_bir,create_manager=create_manager,alert = alert)
        self.assertEqual(get,True)

if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    testcase = unittest.TestLoader().loadTestsFromTestCase(TestAddCustomer)
    suite.addTests(testcase)
    date_now = time.strftime('%Y-%m-%d', time.localtime())
    with open('../../report/AddCustomer_test_report_.html', 'wb+') as file:
    #with open('../../report/AddCustomer_test_report_' + date_now + '_.html', 'wb+') as file:
        runner = HTMLTestRunner(stream=file, verbosity=2, title='Login_auto_test', description='ui_test')
        runner.run(suite)

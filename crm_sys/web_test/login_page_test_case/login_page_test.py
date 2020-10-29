import time
import unittest
from HTMLTestRunner import HTMLTestRunner

import sys
sys.path.append('E:\\.jenkins\\workspace\\test_git')
from crm_sys.base.use_browser import UseBrowser


from crm_sys.web_page.loginpage.login_page import Login
from crm_sys.util.excel_operation import OperationExcel



class TestLogin(unittest.TestCase):
    def setUp(self) -> None:
        self.op = OperationExcel('../../config/test_case.xlsx', '登录用例参数')
        self.login_page=Login(self.op.get_cell(1,1))
        self.bo = self.login_page.bo
    def tearDown(self) -> None:
        UseBrowser.quit()
    def test_login_uname_pwd_null(self):
        self.op = OperationExcel('../../config/test_case.xlsx', '登录用例参数')
        self.login_page.login_func(self.op.get_cell(1,2),self.op.get_cell(1,3))
        alert = self.bo.get_alert()
        self.assertEqual(alert,self.op.get_cell(1,4))
    def test_login_success(self):
        self.op = OperationExcel('../../config/test_case.xlsx', '登录用例参数')
        self.login_page.login_func(self.op.get_cell(2,2), self.op.get_cell(2,3))
        test = self.bo.get_title()
        self.assertEqual(test,self.op.get_cell(2,4))
    def test_login_error (self):
        self.op = OperationExcel('../../config/test_case.xlsx', '登录用例参数')
        self.login_page.login_func(self.op.get_cell(3,2), self.op.get_cell(3,3))
        test = self.bo.get_alert()
        self.assertEqual(test,self.op.get_cell(3,4))
    def test_login_uname_null (self):
        self.op = OperationExcel('../../config/test_case.xlsx', '登录用例参数')
        self.login_page.login_func(self.op.get_cell(4, 2), self.op.get_cell(4, 3))
        test = self.bo.get_alert()
        self.assertEqual(test, self.op.get_cell(4, 4))
    def test_login_pwd_null (self):
        self.op = OperationExcel('../../config/test_case.xlsx', '登录用例参数')
        self.login_page.login_func(self.op.get_cell(5, 2), self.op.get_cell(5, 3))
        test = self.bo.get_alert()
        self.assertEqual(test, self.op.get_cell(5, 4))


if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    testcase = unittest.TestLoader().loadTestsFromTestCase(TestLogin)
    suite.addTests(testcase)
    date_now = time.strftime('%Y-%m-%d', time.localtime())
    with open('../../report/Login_test_report_.html', 'wb+') as file:
    # with open('../../report/Login_test_report_' + date_now + '_.html', 'wb+') as file:
        runner = HTMLTestRunner(stream=file, verbosity=2, title='Login_auto_test', description='ui_test')
        runner.run(suite)

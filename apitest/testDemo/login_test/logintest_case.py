import unittest
from apitest.testDemo.utils.log import Log
from ddt import ddt, data
from apitest.testDemo.utils.doxlsx import DoExcel
from apitest.testDemo.login_test.request_tools import RequestApi
import pytest



file_name='D:/pyworkpase/apiautos/apitest/testDemo/testData/logindata .xlsx'
sheet_name='login'
test_data = DoExcel(file_name, sheet_name).get_data()

logger = Log()


@ddt
class LoginTestCase(unittest.TestCase):

    def setUp(self) -> None:
        print("start setup")

    @data(*test_data)
    def test_login_01(self, item):  # 登录测试用例

        res = RequestApi(url=item['http'], data=eval(item['data']), method=item['method'],
                         headers=eval(item['header'])).req()
        try:
            self.assertEqual(item['expect'], res)
            test_result='PASS'
        except AssertionError as e:
            test_result='FAILED'
            raise e
        finally:
            DoExcel.write_excel(file_name,sheet_name,item['case_id']+1,res,test_result)
    def tearDown(self) -> None:
        print("end tearDown")


if __name__ == '__main__':
    pytest.main(['-v','logintest_case.py'])
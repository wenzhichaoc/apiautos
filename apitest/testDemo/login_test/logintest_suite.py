import unittest
from logintest_case import LoginTestCase
from apitest.testDemo.utils.A_WQRFhtmlRunner import HTMLTestRunner















suite = unittest.TestSuite()
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(LoginTestCase))
with open('../reports/testreports.html', 'wb') as file:
    runner = HTMLTestRunner(stream=file, verbosity=2, title='登录测试报告', description='就是生成登录测试报告')
    runner.run(suite)

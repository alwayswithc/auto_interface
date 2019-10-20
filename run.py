import unittest
import HTMLTestRunner
from tools.project_path import *
from tools.test_http_request import TestHttpRequest

suite=unittest.TestSuite()
#suite.addTest(TestHttpRequest('test_api')) #测试类的实例
loader=unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(TestHttpRequest))

with open(test_report_path,'wb')as file:
    runner=HTMLTestRunner.HTMLTestRunner(stream=file,
    title='测试报告',
    description='用例执行情况：')
    runner.run(suite)
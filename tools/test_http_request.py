import unittest
from tools.do_excel import DoExcel
from tools.project_path import *
from ddt import *
from tools.http_request import HttpRequest
from tools.get_cookie import GetCookie
from tools.my_log import MyLog

test_data=DoExcel.get_data(test_case_path)
@ddt
class TestHttpRequest(unittest.TestCase):
    def setUp(self):
        pass
    @data(*test_data)
    def test_api(self,item):
        res=HttpRequest.http_request(item['method'],item['url'],eval(item['data']),getattr(GetCookie,'Cookie'))
        if res.cookies: #利用反射存储cookie值
            setattr(GetCookie,'Cookie',res.cookies)
        try:
            self.assertEqual(str(item['expected']),res.json()['resultcode'])
            TestResult='PASS'
        except AssertionError as e:
            TestResult='Failed'
            MyLog.error("执行用例出错:{0}".format(e))
            raise e
        finally:
            DoExcel.write_back(test_case_path,item['sheet_name'],item['case_id']+1,res.text,TestResult)
            MyLog.info("获取到的结果是：{0}".format(res.text))
    def tearDown(self):
        pass
if __name__ == '__main__':
    unittest.main(verbosity=2)

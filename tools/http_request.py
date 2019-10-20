import requests
from tools.my_log import MyLog
class HttpRequest:
    @staticmethod
    def http_request(method,url,data,cookie=None):
        try:
            if method.upper()=='GET':
                res=requests.get(url,data,cookies=cookie)
            elif method.upper() == 'POST':
                res=requests.post(url,data,cookies=cookie)
            else:
                MyLog.info("请求的方法不对")
        except Exception as e:
            MyLog.error("请求报错了：{0}".format(e))
            raise e
        return res

            
            
        
        
import mysql.connector
from tools.read_config import ReadConfig
from tools.project_path import *
class DoMySQL:
    def do_mysql(self,query,state='all'):    #query-->查询语句
        config=eval(ReadConfig.read_config(test_config_path,'DB','config'))
        #创建一个数据库连接
        cnn = mysql.connector.connect(**config)
        #游标cursor
        cursor=cnn.cursor()
        #执行语句
        cursor.execute(query)
        #获取结果 打印结果
        if state==1:
            res=cursor.fetchone() #针对一条数据 返回的是元组
        else:
            res=cursor.fetchall() #针对多条数据 返回的是列表
        #关闭游标
        cursor.close()
        #关闭连接
        cnn.close()
        return res
if __name__ == '__main__':
    do=DoMySQL()
    #res=do.do_mysql('select * from books where id=1')
    #print(res[0][0])
    res=do.do_mysql('select * from books where id=1',1)
    print(res[0])


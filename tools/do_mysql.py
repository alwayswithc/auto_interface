import mysql.connector
config={
    'host':'127.0.0.1',
    'user':'root',
    'password':'123456',
    'port':3306,
    'database':'bookmall',
}
#创建一个数据库连接
cnn = mysql.connector.connect(**config)
#游标cursor
cursor=cnn.cursor()
#写sql语句
query_sql='select * from books where id=1'
#执行语句
cursor.execute(query_sql)
#获取结果 打印结果
res=cursor.fetchone() #针对一条数据 返回的是元组
#cursor.fetchall() 针对多条数据 返回的是列表
print(res)
#关闭游标
cursor.close()
#关闭连接
cnn.close()

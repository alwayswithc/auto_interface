import logging

#logger 收集日志
#handdler 输出日志的渠道 指定的文件 还是控制台（默认控制台）
# logging.debug()
# logging.info()
# logging.warning()
# logging.error()
# logging.critical()

#定义一个日志收集器 my_logger
my_logger=logging.getLogger()
#设定级别
my_logger.setLevel('DEBUG')

#创建一个我们自己的输出渠道
ch=logging.StreamHandler()
ch.setLevel('DEBUG')
fh=logging.FileHandler('log.txt',encoding='utf-8')
fh.setLevel('DEBUG')

#formatter:决定日志记录的最终输出格式（不然日志会乱七八糟的）Formatter对象定义了最终log信息的顺序，结构和内容
formatter=logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息：%(message)s')
ch.setFormatter(formatter)
fh.setFormatter(formatter)

#两者对接
my_logger.addHandler(ch)
my_logger.addHandler(fh)
#收集日志
my_logger.debug('python自动化测试学习')
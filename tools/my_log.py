import logging
from tools.project_path import *
class MyLog:
    @staticmethod
    def my_log(msg,level):

        #定义一个日志收集器 my_logger
        my_logger = logging.getLogger()
        # 设定级别
        my_logger.setLevel('DEBUG')

        # 创建一个我们自己的输出渠道
        ch = logging.StreamHandler()
        ch.setLevel('DEBUG')
        fh = logging.FileHandler(log_path, encoding='utf-8')
        fh.setLevel('DEBUG')

        # formatter:决定日志记录的最终输出格式（不然日志会乱七八糟的）Formatter对象定义了最终log信息的顺序，结构和内容
        formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息：%(message)s')
        ch.setFormatter(formatter)
        fh.setFormatter(formatter)

        # 两者对接
        my_logger.addHandler(ch)
        my_logger.addHandler(fh)

        if level=='DEBUG':
            my_logger.debug(msg)
        elif level=='INFO':
            my_logger.info(msg)
        elif level=='WARNING':
            my_logger.warning(msg)
        elif level=='ERROR':
            my_logger.error(msg)
        elif level=='CRITICAL':
            my_logger.critical(msg)

    @staticmethod
    def debug(msg):
        MyLog.my_log(msg,'DEBUG')

    @staticmethod
    def info(msg):
        MyLog.my_log(msg,'INFO')

    @staticmethod
    def warning(msg):
        MyLog.my_log(msg,'WARNING')

    @staticmethod
    def error(msg):
        MyLog.my_log(msg, 'ERROR')

    @staticmethod
    def critical(msg):
        MyLog.my_log(msg, 'CRITICAL')
if __name__ == '__main__':
    MyLog.debug('ccccmmmm')





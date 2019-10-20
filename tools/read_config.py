import configparser
class ReadConfig:
    @staticmethod
    def read_config(file_name,section,option):
        cf=configparser.ConfigParser()
        cf.read(file_name,encoding='utf-8')
        return cf.get(section,option)
# if __name__ == '__main__':
#    re= ReadConfig.read_config('../conf/case.config','MODE','mode')
#    print(re)
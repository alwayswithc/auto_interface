import os
'''专门用来读取路径的值'''
project_path=os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
# C:\Users\12231\PycharmProjects\interface_auto
#测试用例的路径
test_case_path=os.path.join(project_path,'test_data','test_data.xlsx')
#测试报告的路径
test_report_path=os.path.join(project_path,'test_result','html_report','test_api.html')
#配置文件的路径
test_config_path=os.path.join(project_path,'conf','case.config')
#日志的路径
log_path=os.path.join(project_path,'test_result','log.txt')

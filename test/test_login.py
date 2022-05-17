# 引入框架pytest
import pytest
import os
import copy
from configs.config import HOST_ZY
from req.login import Login
from tools.yamlControl import get_yaml_data
from tools.loggerHandler import logger
"""
方案：数据驱动
        1- 用例的响应参数
        2- 用例的期望结果
"""

# 登录接口-测试类封装
class TestLogin(object):
    # 测试方法
    @pytest.mark.parametrize('detail, inBody, expData', get_yaml_data('../case/loginCase.yaml'))  # 数据驱动方法
    def test_login(self, detail, inBody, expData):
        # 调用业务代码
        data = copy.deepcopy(inBody)
        res = Login().login(inBody, False)
        try:
            # 断言
            assert expData['msg'] in res["msg"]
            # 记录日志
            logger.info('测试用例："{0}"，用户名{1}，密码{2}，请求响应状态"{3}"，测试用例状态"{4}"，断言成功'.format
                        (detail, data["loginName"], data["password"], res["msg"], expData['msg']))
        except AssertionError:
            # 记录日志
            logger.error('测试用例："{0}"，用户名{1}，密码{2}，请求响应状态"{3}"，测试用例状态"{4}"，断言失败'.format
                         (detail, data["loginName"], data["password"], res["msg"], expData['msg']))


if __name__ == '__main__':
    #运行测试用例
    pytest.main(['test_login.py', '-s', '--alluredir', '../report/login', '--clean-alluredir'])
    #查看allure产生报告
    # os.system('allure serve ../report/login')

# 引入框架pytest
import pytest
import os
import copy
from req.login import Login
from req.carlist import CarList
from tools.yamlControl import get_yaml_data
from tools.loggerHandler import logger

# 车辆列表接口-测试类封装
class TestCarLists(object):
    # 测试方法
    @pytest.mark.parametrize('detail,inBody,expData', get_yaml_data('../case/carlistCase.yaml'))  # 数据驱动方法
    def test_car_list(self, detail, inBody, expData):
        # 调用业务代码
        data = copy.deepcopy(inBody)
        heard = {'token':Login().login()}
        res=CarList().car_list(data,heard)
        try:
            # 断言
            assert expData['msg'] in res["msg"]
            # 记录日志
            logger.info('测试用例："{0}"，每页条数{1}，页数{2}，请求响应状态"{3}"，测试用例状态"{4}"，断言成功'.format
                        (detail, data["pageSize"], data["pageNumber"], res["msg"], expData['msg']))
        except AssertionError:
            # 记录日志
            logger.error('测试用例："{0}"，每页条数{1}，页数{2}，请求响应状态"{3}"，测试用例状态"{4}"，断言失败'.format
                         (detail, data["pageSize"], data["pageNumber"], res["msg"], expData['msg']))



if __name__ == '__main__':
    # 运行测试用例
    pytest.main([ '-s', '--alluredir', '../report/login', '--clean-alluredir'])
    # 查看allure产生报告
    # os.system('allure serve ../report/login')

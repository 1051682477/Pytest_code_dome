from configs.config import HOST_ZY
import hashlib
import requests
import pytest
from tools.yamlControl import get_yaml_data

class CarList(object):

    @pytest.mark.parametrize('', get_yaml_data('../case/carlistCase.yaml'))
    def car_list(self, car_list_data,header):
        # url路径
        url = str(HOST_ZY) + '/enterprise/netVehiclePage'
        # 参数
        payload = car_list_data
        # 请求
        """
        data   ----- 一般是表单格式
        json   ----- json
        files  ----- 文件上传接口
        params ----- 以'?a=1&b=2'形式放在url路径里
        """
        resp = requests.post(url,data=payload,headers=header)
        return resp.json()


if __name__ == '__main__':
    from req.login import Login
    token=Login().login()
    res = CarList().car_list(car_list_data={'pageSize':10,'pageNumber':1},header={'token':token})
    print(res)
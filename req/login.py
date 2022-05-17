"""
接口名称：登录接口
接口类型：token机制
用途：
    1- 本身需要做接口自动化测试
    2- 获取token，给后续的接口做鉴权
"""
from configs.config import HOST_ZY
import hashlib
import requests
import pytest
from tools.yamlControl import get_yaml_data

# 封装一个登陆类



class Login(object):
    #暂时无需加密 根据接口文档调整加密方式
    def get_md5(self, psw):
        """
        MD5加密方法
        :param psw: 输入登录密码
        :return: 返回MD5加密结果
        """
        # 实例化一个MD5对象
        md5 = hashlib.md5()
        # 调用加密方法直接加密
        md5.update(psw.encode('utf-8'))
        return md5.hexdigest()

    @pytest.mark.parametrize('', get_yaml_data('../case/loginCase.yaml'))
    def login(self, login_data={'loginName': 'hn-zz-sljt', 'password': 'zh123456','captcha': '12'}, mode=True):
        # url路径
        url = str(HOST_ZY)+'/login'
        # login_data['password'] = self.get_md5(login_data['password'])
        # 参数
        payload = login_data
        # 请求
        """
        data   ----- 一般是表单格式
        json   ----- json
        files  ----- 文件上传接口
        params ----- 以'?a=1&b=2'形式放在url路径里
        """
        resp = requests.post(url, data=payload)
        # 获取token模式/获取登录信息模式
        if mode:
            return resp.json()['data']['token']
        else:
            return resp.json()


if __name__ == '__main__':
    res = Login().login(mode=False)
    print(res)

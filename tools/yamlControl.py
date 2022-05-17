import yaml


def get_yaml_data(fileDir, mode=False):
    # 1- 读取文件
    fo = open(fileDir, 'r', encoding='utf-8')
    # 2- 使用yaml方法获取数据
    res = yaml.load(fo, Loader=yaml.FullLoader)
    # 3- 关闭文件
    fo.close()
    if mode:
        return res
    else:
        # 存放结果
        resList = []  # [(请求1，期望响应1), (请求2，期望响应2), ...]
        for item in res[1:]:
            resList.append((item['detail'], item['data'], item["resp"]))
        return resList


if __name__ == '__main__':
    data_resp = get_yaml_data('../case/carlistCase.yaml')
    data_resp_login=get_yaml_data('../case/loginCase.yaml')
    print(data_resp_login)
    print(data_resp)
    log_resp = get_yaml_data('../configs/logConfig.yaml', True)
    print(log_resp)

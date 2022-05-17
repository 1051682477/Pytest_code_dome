import pytest


# 自动化测试执行前，环境初始化操作
@pytest.fixture(scope='session', autouse=True)
def start_running():
    print('----马上开始执行自动化测试----')
    yield
    print('----自动化测试完成，开始处理本次测试数据----')
# 自动化测试完成之后，数据清除操作

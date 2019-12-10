import unittest

from parameterized import parameterized
import requests

from api.api_login import ApiLogin


# 定义函数
# def get_data():
#     return [("13800001111", "123456", "8888", 1), ("13800001121", "123456", "8888", -1),
#             ("13800001111", "1234567", "8888", -2)]
from tools.read_json import read_json


class TestLogin(unittest.TestCase):
    # 初始化
    @classmethod
    def setUpClass(cls):
        # 获取session对象
        cls.session = requests.session()
        # 获取ApiLogin对象
        cls.login = ApiLogin(cls.session)

    @classmethod
    # 结束
    def tearDownClass(cls):
        # 关闭session对象
        cls.session.close()

    # 测试方法
    @parameterized.expand(read_json("login.json"))
    def test_login(self, username, password, verify_code, expect):
        # 调用 获取验证码
        self.login.api_verify_code()
        # 调用 登录
        r = self.login.api_login(username, password, verify_code)
        # 断言
        self.assertEqual(expect, r.json().get("status"))

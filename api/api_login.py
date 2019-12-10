class ApiLogin:
    def __init__(self, session):
        self.session = session
        self.url_code = "http://localhost/index.php?m=Home&c=User&a=verify"
        self.url_login = "http://localhost/index.php?m=Home&c=User&a=do_login"

    # 验证码
    def api_verify_code(self):
        self.session.get(url=self.url_code)

    # 登录
    def api_login(self, username, password, verify_code):
        """
        :param session: session对象
        :param username: 用户名
        :param password: 密码
        :param verify_code: 验证码
        :return: 登录后的响应的对象
        """
        data = {"username":username, "password":password, "verify_code":verify_code}
        return self.session.post(url=self.url_login, data=data)
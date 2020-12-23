import pytest
from data.login_data import LoginData

# 改变输出结果
success_ids = [
    "测试：{}->[用户名:{}-密码:{}-预期:{}]".
        format(data["case"], data["username"], data["password"], data["expected"]) for data in LoginData.login_success_data
]


@pytest.mark.loginTest
class Test_Login(object):
    """登录测试"""
    login_data = LoginData

    @pytest.mark.parametrize("data", login_data.login_success_data, ids=success_ids)
    def test_login(self, open_url, data):
        """登录测试"""
        login_page = open_url
        login_page.login(data["username"],data["password"])
        result = login_page.login_text()
        assert data["expected"] == result, "登录成功， 断言失败"


if __name__ == "__main__":
    pytest.main(['-v', 'test_loginCase.py'])

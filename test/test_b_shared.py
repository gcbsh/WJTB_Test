import pytest
from data.shared_data import SharedData

# 改变输出结果
test_success_ids = [
    "测试：{}->[预期:{}]".
        format(data["case"],  data["expected"]) for data in SharedData.test_success_data
]


@pytest.mark.loginTest
class Test_Shared(object):
    """创建共享目录测试"""
    shared_data = SharedData

    @pytest.mark.parametrize("data", shared_data.test_success_data, ids=test_success_ids)
    def test_shared(self, login, data):
        """填写正确信息，创建内端共享目录测试"""
        shared_page = login[1]
        result = shared_page.shared()
        result2 = shared_page.save_text()
        assert data["expected"] == result and data["expected1"] == result2, "创建内端共享目录成功， 断言成功"

    @pytest.mark.parametrize("data", shared_data.test_success_data, ids=test_success_ids)
    def test_shared_nfs(self, login, data):
        """填写正确信息，创建内端nfs共享目录测试"""
        shared_page = login[1]
        result = shared_page.shared_nfs()
        result2 = shared_page.save_text()
        assert data["expected"] == result and data["expected1"] == result2, "创建内端共享目录成功， 断言成功"

    @pytest.mark.parametrize("data", shared_data.test_success_data, ids=test_success_ids)
    def test_shared_wai(self, login, data):
        """填写正确信息，创建外端共享目录测试"""
        shared_page = login[1]
        result = shared_page.shared_wai()
        result2 = shared_page.save_text()
        assert data["expected"] == result and data["expected1"] == result2, "创建外端共享目录成功， 断言成功"

    @pytest.mark.parametrize("data", shared_data.test_success_data, ids=test_success_ids)
    def test_shared_nfs_wai(self, login, data):
        """填写正确信息，创建外端nfs共享目录测试"""
        shared_page = login[1]
        result = shared_page.shared_nfs_wai()
        result2 = shared_page.save_text()
        assert data["expected"] == result and data["expected1"] == result2, "创建外端共享目录成功， 断言成功"








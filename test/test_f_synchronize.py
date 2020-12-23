import pytest
from data.synchronize_data import SynchronizeData

# 改变输出结果
create_task_ids = [
    "测试：{}->[预期:{}]".
        format(data["case"],  data["expected"]) for data in SynchronizeData.create_task_data
]


@pytest.mark.loginTest
class TestSynchronize(object):
    """创建共享目录测试"""
    synchronize_data = SynchronizeData

    @pytest.mark.parametrize("data", synchronize_data.create_task_data, ids=create_task_ids)
    def test_shared(self, login, data):
        """创建同步任务，任务启用，任务停止测试"""
        synchronize_page = login[2]
        result = synchronize_page.create_task()
        result3 = synchronize_page.save_task_text()
        assert data["expected"] == result[0] and data["expected1"] == result[1] and data["expected2"] == result3, "创建内端共享目录成功， 断言成功"


if __name__ == "__main__":
    pytest.main()

import pytest
from data.content_data import ContentData

# 改变输出结果

add_content_none_ids = [
    "测试：{}->[预期:{}]".
        format(data["case"],  data["expected"]) for data in ContentData.add_content_none_data
]
add_content_cancel_ids = [
    "测试：{}->[预期:{}]".
        format(data["case"],  data["expected"]) for data in ContentData.add_content_cancel_data
]
add_content_Chinese_ids = [
    "测试：{}->[预期:{}]".
        format(data["case"],  data["expected"]) for data in ContentData.add_content_Chinese_data
]
add_content_English_ids = [
    "测试：{}->[预期:{}]".
        format(data["case"],  data["expected"]) for data in ContentData.add_content_English_data
]
add_content_english_ids = [
    "测试：{}->[预期:{}]".
        format(data["case"],  data["expected"]) for data in ContentData.add_content_english_data
]
add_content_number_ids = [
    "测试：{}->[预期:{}]".
        format(data["case"],  data["expected"]) for data in ContentData.add_content_number_data
]
add_content_halfSymbol_ids = [
    "测试：{}->[预期:{}]".
        format(data["case"],  data["expected"]) for data in ContentData.add_content_halfSymbol_data
]
add_content_entireSymbol_ids = [
    "测试：{}->[预期:{}]".
        format(data["case"],  data["expected"]) for data in ContentData.add_content_entireSymbol_data
]
add_content_halfSpace_ids = [
    "测试：{}->[预期:{}]".
        format(data["case"],  data["expected"]) for data in ContentData.add_content_halfSpace_data
]
add_content_entireSpace_ids = [
    "测试：{}->[预期:{}]".
        format(data["case"],  data["expected"]) for data in ContentData.add_content_entireSpace_data
]
add_content_superLong64_ids = [
    "测试：{}->[预期:{}]".
        format(data["case"],  data["expected"]) for data in ContentData.add_content_superLong64_data
]
add_content_superLong65_ids = [
    "测试：{}->[预期:{}]".
        format(data["case"],  data["expected"]) for data in ContentData.add_content_superLong65_data
]
search_content_chinese_ids = [
    "测试：{}->[预期:{}]".
        format(data["case"],  data["expected"]) for data in ContentData.search_content_chinese_data
]
search_content_English_ids = [
    "测试：{}->[预期:{}]".
        format(data["case"],  data["expected"]) for data in ContentData.search_content_English_data
]
search_content_english_ids = [
    "测试：{}->[预期:{}]".
        format(data["case"],  data["expected"]) for data in ContentData.search_content_english_data
]
search_content_number_ids = [
    "测试：{}->[预期:{}]".
        format(data["case"],  data["expected"]) for data in ContentData.search_content_number_data
]
search_content_halfSymbol_ids = [
    "测试：{}->[预期:{}]".
        format(data["case"],  data["expected"]) for data in ContentData.search_content_halfSymbol_data
]
search_content_entireSymbol_ids = [
    "测试：{}->[预期:{}]".
        format(data["case"],  data["expected"]) for data in ContentData.search_content_entireSymbol_data
]
delete_content_noSelect_ids = [
    "测试：{}->[预期:{}]".
        format(data["case"],  data["expected"]) for data in ContentData.delete_content_noSelect_data
]
delete_content_single_ids = [
    "测试：{}->[预期:{}]".
        format(data["case"],  data["expected"]) for data in ContentData.delete_content_single_data
]
delete_content_singleEmploy_ids = [
    "测试：{}->[预期:{}]".
        format(data["case"],  data["expected"]) for data in ContentData.delete_content_singleEmploy_data
]
delete_content_multipleChoice_ids = [
    "测试：{}->[预期:{}]".
        format(data["case"],  data["expected"]) for data in ContentData.delete_content_multipleChoice_data
]
delete_content_allSelect_ids = [
    "测试：{}->[预期:{}]".
        format(data["case"],  data["expected"]) for data in ContentData.delete_content_allSelect_data
]

#导入文件内容数据
content_name = ContentData.test_content_data

@pytest.mark.loginTest
class Test_content(object):
    """文件内容过滤测试"""
    content_data = ContentData

    @pytest.mark.parametrize("data", content_data.add_content_none_data, ids=add_content_none_ids)
    def test_add_content_none(self, login, refresh_page, data):
        """添加文件内容过滤测试,为空(直接保存)"""
        content_page = login[5]
        content_page.add_content_none()
        result = content_page.content_error_text()
        assert data["expected"] in result, "添加失败， 断言失败"

    @pytest.mark.parametrize("data", content_data.add_content_cancel_data, ids=add_content_cancel_ids)
    def test_add_content_cancel(self, login, refresh_page, data):
        """添加文件内容过滤测试,取消"""
        content_page = login[5]
        content_page.add_content_cancel()
        result = content_page.content_cancel_text()
        assert data["expected"] in result, "添加失败， 断言失败"

    @pytest.mark.parametrize("data", content_data.add_content_Chinese_data, ids=add_content_Chinese_ids)
    def test_add_content_Chinese(self, login, refresh_page, data):
        """添加文件内容过滤测试,中文"""
        content_page = login[5]
        content_page.add_content_process(content_name[0])
        result = content_page.save_content_text()
        assert data["expected"] in result, "添加成功， 断言成功"

    @pytest.mark.parametrize("data", content_data.add_content_English_data, ids=add_content_English_ids)
    def test_add_content_English(self, login, refresh_page, data):
        """添加文件内容过滤测试,英文大写"""
        content_page = login[5]
        content_page.add_content_process(content_name[1])
        result = content_page.save_content_text()
        assert data["expected"] in result, "添加成功， 断言成功"

    @pytest.mark.parametrize("data", content_data.add_content_english_data, ids=add_content_english_ids)
    def test_add_content_english(self, login, refresh_page, data):
        """添加文件内容过滤测试,英文小写"""
        content_page = login[5]
        content_page.add_content_process(content_name[2])
        result = content_page.save_content_text()
        assert data["expected"] in result, "添加成功， 断言成功"

    @pytest.mark.parametrize("data", content_data.add_content_number_data, ids=add_content_number_ids)
    def test_add_content_number(self, login, refresh_page, data):
        """添加文件内容过滤测试,数字"""
        content_page = login[5]
        content_page.add_content_process(content_name[3])
        result = content_page.save_content_text()
        assert data["expected"] in result, "添加成功， 断言成功"

    @pytest.mark.parametrize("data", content_data.add_content_halfSymbol_data, ids=add_content_halfSymbol_ids)
    def test_add_content_halfSymbol(self, login, refresh_page, data):
        """添加文件内容过滤测试,半角符号"""
        content_page = login[5]
        content_page.add_content_process(content_name[4])
        result = content_page.save_content_text()
        assert data["expected"] in result, "添加成功， 断言成功"

    @pytest.mark.parametrize("data", content_data.add_content_entireSymbol_data, ids=add_content_entireSymbol_ids)
    def test_add_content_entireSymbol(self, login, refresh_page, data):
        """添加文件内容过滤测试,全角符号"""
        content_page = login[5]
        content_page.add_content_process(content_name[5])
        result = content_page.save_content_text()
        assert data["expected"] in result, "添加成功， 断言成功"

    @pytest.mark.parametrize("data", content_data.add_content_halfSpace_data, ids=add_content_halfSpace_ids)
    def test_add_content_halfSpace(self, login, refresh_page, data):
        """添加文件内容过滤测试,仅有半角空格"""
        content_page = login[5]
        content_page.add_content_process(content_name[6])
        result = content_page.content_error_text()
        assert data["expected"] in result, "添加失败， 断言失败"

    @pytest.mark.parametrize("data", content_data.add_content_entireSpace_data, ids=add_content_entireSpace_ids)
    def test_add_content_entireSpace(self, login, refresh_page, data):
        """添加文件内容过滤测试,仅有全角空格"""
        content_page = login[5]
        content_page.add_content_process(content_name[7])
        result = content_page.content_error_text()
        assert data["expected"] in result, "添加失败， 断言失败"

    @pytest.mark.parametrize("data", content_data.add_content_superLong64_data, ids=add_content_superLong64_ids)
    def test_add_content_superLong64(self, login, refresh_page, data):
        """添加文件内容过滤测试,超长字符64位"""
        content_page = login[5]
        content_page.add_content_process(content_name[8])
        result = content_page.save_content_text()
        assert data["expected"] in result, "添加成功， 断言成功"

    @pytest.mark.parametrize("data", content_data.add_content_superLong65_data, ids=add_content_superLong65_ids)
    def test_add_content_superLong65(self, login, refresh_page, data):
        """添加文件内容过滤测试,超长字符65位"""
        content_page = login[5]
        content_page.add_content_process(content_name[9])
        result = content_page.content_error_text()
        assert data["expected"] in result, "添加失败， 断言失败"

    @pytest.mark.parametrize("data", content_data.search_content_chinese_data, ids=search_content_chinese_ids)
    def test_search_content_chinese(self, login, refresh_page, data):
        """搜索文件内容过滤测试,中文搜索"""
        content_page = login[5]
        content_page.search_content_process(content_name[0])
        result = content_page.content_search_text()
        assert data["expected"] in result, "搜索成功， 断言成功"

    @pytest.mark.parametrize("data", content_data.search_content_English_data, ids=search_content_English_ids)
    def test_search_content_English(self, login, refresh_page, data):
        """搜索文件内容过滤测试,英文大写搜索"""
        content_page = login[5]
        content_page.search_content_process(content_name[1])
        result = content_page.content_search_text()
        assert data["expected"] in result, "搜索成功， 断言成功"

    @pytest.mark.parametrize("data", content_data.search_content_english_data, ids=search_content_english_ids)
    def test_search_content_english(self, login, refresh_page, data):
        """搜索文件内容过滤测试,英文小写搜索"""
        content_page = login[5]
        content_page.search_content_process(content_name[2])
        result = content_page.content_search_text()
        assert data["expected"] in result, "搜索成功， 断言成功"

    @pytest.mark.parametrize("data", content_data.search_content_number_data, ids=search_content_number_ids)
    def test_search_content_number(self, login, refresh_page, data):
        """搜索文件内容过滤测试,数字搜索"""
        content_page = login[5]
        content_page.search_content_process(content_name[3])
        result = content_page.content_search_text()
        assert data["expected"] in result, "搜索成功， 断言成功"

    @pytest.mark.xfail(condition=2>1,reason="&被编译")
    @pytest.mark.parametrize("data", content_data.search_content_halfSymbol_data, ids=search_content_halfSymbol_ids)
    def test_search_content_halfSymbol(self, login, refresh_page, data):
        """搜索文件内容过滤测试,半角符号搜索"""
        content_page = login[5]
        content_page.search_content_process(content_name[4])
        result = content_page.content_search_text()
        assert data["expected"] in result, "搜索成功， 断言成功"


    @pytest.mark.parametrize("data", content_data.search_content_entireSymbol_data, ids=search_content_entireSymbol_ids)
    def test_search_content_entireSymbol(self, login, refresh_page, data):
        """搜索文件内容过滤测试,全角符号搜索"""
        content_page = login[5]
        content_page.search_content_process(content_name[5])
        result = content_page.content_search_text()
        assert data["expected"] in result, "搜索成功， 断言成功"

    @pytest.mark.parametrize("data", content_data.delete_content_noSelect_data, ids=delete_content_noSelect_ids)
    def test_delete_content_noSelect(self, login, refresh_page, data):
        """删除文件内容过滤测试,不选择列表"""
        content_page = login[5]
        content_page.delete_content_noSeletect()
        result = content_page.content_error_text()
        assert data["expected"] in result, "删除失败， 断言失败"

    @pytest.mark.parametrize("data", content_data.delete_content_single_data, ids=delete_content_single_ids)
    def test_delete_content_single(self, login, refresh_page, data):
        """删除文件内容过滤测试,单选未被任务使用"""
        content_page = login[5]
        content_page.delete_content_single()
        result = content_page.save_content_text()
        assert data["expected"] in result, "删除成功， 断言失败"

    @pytest.mark.xfail(condition=2>1,reason="未建立任务")
    @pytest.mark.parametrize("data", content_data.delete_content_singleEmploy_data, ids=delete_content_singleEmploy_ids)
    def test_delete_content_singleEmploy(self, login, refresh_page, data):
        """删除文件内容过滤测试,单选被任务使用"""
        content_page = login[5]
        content_page.delete_content_singleEmploy()
        result = content_page.save_content_text()
        assert data["expected"] in result, "添加失败， 断言失败"

    @pytest.mark.parametrize("data", content_data.delete_content_multipleChoice_data, ids=delete_content_multipleChoice_ids)
    def test_delete_content_multipleChoice(self, login, refresh_page, data):
        """删除文件内容过滤测试,多选"""
        content_page = login[5]
        content_page.delete_content_multipleChoice()
        result = content_page.save_content_text()
        assert data["expected"] in result, "添加失败， 断言失败"

    @pytest.mark.parametrize("data", content_data.delete_content_allSelect_data, ids=delete_content_allSelect_ids)
    def test_delete_content_allSelect(self, login, refresh_page, data):
        """删除文件内容过滤测试,全选"""
        content_page = login[5]
        content_page.delete_content_allSelect()
        result = content_page.save_content_text()
        assert data["expected"] in result, "删除成功， 断言失败"

if __name__ == "__main__":
    pytest.main()

import pytest
from data.suffix_data import SuffixData

# 改变输出结果
add_suffix_Chinese_ids = [
    "测试：{}->[预期:{}]".
        format(data["case"],  data["expected"]) for data in SuffixData.add_suffix_Chinese_data
]
add_suffix_English_ids = [
    "测试：{}->[预期:{}]".
        format(data["case"],  data["expected"]) for data in SuffixData.add_suffix_English_data
]
add_suffix_english_ids = [
    "测试：{}->[预期:{}]".
        format(data["case"],  data["expected"]) for data in SuffixData.add_suffix_english_data
]
add_suffix_number_ids = [
    "测试：{}->[预期:{}]".
        format(data["case"],  data["expected"]) for data in SuffixData.add_suffix_number_data
]
add_suffix_halfSymbol_ids = [
    "测试：{}->[预期:{}]".
        format(data["case"],  data["expected"]) for data in SuffixData.add_suffix_halfSymbol_data
]
add_suffix_entireSymbol_ids = [
    "测试：{}->[预期:{}]".
        format(data["case"],  data["expected"]) for data in SuffixData.add_suffix_entireSymbol_data
]
add_suffix_superLong64_ids = [
    "测试：{}->[预期:{}]".
        format(data["case"],  data["expected"]) for data in SuffixData.add_suffix_superLong64_data
]
add_suffix_superLong65_ids = [
    "测试：{}->[预期:{}]".
        format(data["case"],  data["expected"]) for data in SuffixData.add_suffix_superLong65_data
]
search_suffix_English_ids = [
    "测试：{}->[预期:{}]".
        format(data["case"],  data["expected"]) for data in SuffixData.search_suffix_English_data
]
search_suffix_number_ids = [
    "测试：{}->[预期:{}]".
        format(data["case"],  data["expected"]) for data in SuffixData.search_suffix_number_data
]
search_suffix_halfSymbol_ids = [
    "测试：{}->[预期:{}]".
        format(data["case"],  data["expected"]) for data in SuffixData.search_suffix_halfSymbol_data
]
search_suffix_entireSymbol_ids = [
    "测试：{}->[预期:{}]".
        format(data["case"],  data["expected"]) for data in SuffixData.search_suffix_entireSymbol_data
]
none_suffix_ids = [
    "测试：{}->[预期:{}]".
        format(data["case"],  data["expected"]) for data in SuffixData.none_suffix_data
]
cancel_suffix_ids = [
    "测试：{}->[预期:{}]".
        format(data["case"],  data["expected"]) for data in SuffixData.cancel_suffix_data
]
delete_suffix_noSelect_ids = [
    "测试：{}->[预期:{}]".
        format(data["case"],  data["expected"]) for data in SuffixData.delete_suffix_noSelect_data
]
delete_suffix_single_ids = [
    "测试：{}->[预期:{}]".
        format(data["case"],  data["expected"]) for data in SuffixData.delete_suffix_single_data
]
delete_suffix_employ_ids = [
    "测试：{}->[预期:{}]".
        format(data["case"],  data["expected"]) for data in SuffixData.delete_suffix_employ_data
]
delete_suffix_multipleChoice_ids = [
    "测试：{}->[预期:{}]".
        format(data["case"],  data["expected"]) for data in SuffixData.delete_suffix_multipleChoice_data
]
delete_suffix_allSelect_ids = [
    "测试：{}->[预期:{}]".
        format(data["case"],  data["expected"]) for data in SuffixData.delete_suffix_allSelect_data
]

#导入文件后缀名数据
suffix_name = SuffixData.test_suffix_data

@pytest.mark.loginTest
class Test_Suffix(object):
    """文件后缀名过滤测试"""
    suffix_data = SuffixData

    @pytest.mark.parametrize("data", suffix_data.cancel_suffix_data, ids=cancel_suffix_ids)
    def test_create_suffix_cancel(self, login, refresh_page, data):
        """添加文件后缀名过滤测试,取消"""
        suffix_page = login[4]
        suffix_page.add_suffix_cancel()
        result = suffix_page.cancel_suffix_text()
        assert data["expected"] in result, "添加失败， 断言失败"

    @pytest.mark.parametrize("data", suffix_data.add_suffix_Chinese_data, ids=add_suffix_Chinese_ids)
    def test_create_suffix_Chinese(self, login, refresh_page, data):
        """添加文件后缀名过滤测试,中文后缀"""
        suffix_page = login[4]
        suffix_page.add_suffix_process(suffix_name[0])
        result = suffix_page.add_suffix_exception_text()
        assert data["expected"] in result, "添加失败， 断言失败"

    @pytest.mark.parametrize("data", suffix_data.add_suffix_English_data, ids=add_suffix_English_ids)
    def test_create_suffix_English(self, login, refresh_page, data):
        """添加文件后缀名过滤测试,英文大写后缀"""
        suffix_page = login[4]
        suffix_page.add_suffix_process(suffix_name[1])
        result = suffix_page.add_suffix_exception_text()
        assert data["expected"] in result, "添加失败， 断言失败"

    @pytest.mark.parametrize("data", suffix_data.add_suffix_english_data, ids=add_suffix_english_ids)
    def test_create_suffix_english(self, login, refresh_page, data):
        """添加文件后缀名过滤测试,英文小写后缀"""
        suffix_page = login[4]
        suffix_page.add_suffix_process(suffix_name[2])
        result = suffix_page.add_suffix_text()
        assert data["expected"] in result, "添加成功， 断言成功"

    @pytest.mark.parametrize("data", suffix_data.add_suffix_number_data, ids=add_suffix_number_ids)
    def test_create_suffix_number(self, login, refresh_page, data):
        """添加文件后缀名过滤测试,数字后缀"""
        suffix_page = login[4]
        suffix_page.add_suffix_process(suffix_name[3])
        result = suffix_page.add_suffix_text()
        assert data["expected"] in result, "添加成功， 断言成功"


    @pytest.mark.parametrize("data", suffix_data.add_suffix_halfSymbol_data, ids=add_suffix_halfSymbol_ids)
    def test_create_suffix_halfSymbol(self, login, refresh_page, data):
        """添加文件后缀名过滤测试,半角符号后缀"""
        suffix_page = login[4]
        suffix_page.add_suffix_process(suffix_name[4])
        result = suffix_page.add_suffix_text()
        assert data["expected"] in result, "添加成功， 断言成功"

    @pytest.mark.parametrize("data", suffix_data.add_suffix_entireSymbol_data, ids=add_suffix_entireSymbol_ids)
    def test_create_suffix_entireSymbol(self, login, refresh_page, data):
        """添加文件后缀名过滤测试,全角符号后缀"""
        suffix_page = login[4]
        suffix_page.add_suffix_process(suffix_name[5])
        result = suffix_page.add_suffix_text()
        assert data["expected"] in result, "添加成功， 断言成功"

    @pytest.mark.parametrize("data", suffix_data.add_suffix_superLong64_data, ids=add_suffix_superLong64_ids)
    def test_create_suffix_superLong64(self, login, refresh_page, data):
        """添加文件后缀名过滤测试,超长后缀64位字符"""
        suffix_page = login[4]
        suffix_page.add_suffix_process(suffix_name[6])
        result = suffix_page.add_suffix_text()
        assert data["expected"] in result, "添加成功， 断言成功"

    @pytest.mark.parametrize("data", suffix_data.add_suffix_superLong65_data, ids=add_suffix_superLong65_ids)
    def test_create_suffix_superLong65(self, login, refresh_page, data):
        """添加文件后缀名过滤测试,超长后缀65位字符"""
        suffix_page = login[4]
        suffix_page.add_suffix_process(suffix_name[7])
        result = suffix_page.add_suffix_exception_text()
        assert data["expected"] in result, "添加失败， 断言失败"

    @pytest.mark.parametrize("data", suffix_data.search_suffix_English_data, ids=search_suffix_English_ids)
    def test_search_suffix_English(self, login, refresh_page, data):
        """搜索文件后缀名过滤测试,英文搜索(不区分大小写)"""
        suffix_page = login[4]
        suffix_page.search_suffix_process(suffix_name[2])
        result = suffix_page.search_suffix_text()
        assert data["expected"] in result, "搜索成功， 断言成功"

    @pytest.mark.parametrize("data", suffix_data.search_suffix_number_data, ids=search_suffix_number_ids)
    def test_search_suffix_number(self, login, refresh_page, data):
        """搜索文件后缀名过滤测试,数字搜索"""
        suffix_page = login[4]
        suffix_page.search_suffix_process(suffix_name[3])
        result = suffix_page.search_suffix_text()
        assert data["expected"] in result, "搜索成功， 断言成功"

    @pytest.mark.parametrize("data", suffix_data.search_suffix_halfSymbol_data, ids=search_suffix_halfSymbol_ids)
    def test_search_suffix_halfSymbol(self, login, refresh_page, data):
        """搜索文件后缀名过滤测试,半角字符搜索"""
        suffix_page = login[4]
        suffix_page.search_suffix_process(suffix_name[4])
        result = suffix_page.search_suffix_text()
        assert data["expected"] in result, "搜索成功， 断言成功"

    @pytest.mark.parametrize("data", suffix_data.search_suffix_entireSymbol_data, ids=search_suffix_entireSymbol_ids)
    def test_search_suffix_entireSymbol(self, login, refresh_page, data):
        """搜索文件后缀名过滤测试,全角字符搜索"""
        suffix_page = login[4]
        suffix_page.search_suffix_process(suffix_name[5])
        result = suffix_page.search_suffix_text()
        assert data["expected"] in result, "搜索成功， 断言成功"


    @pytest.mark.parametrize("data", suffix_data.none_suffix_data, ids=none_suffix_ids)
    def test_create_suffix_directSave(self, login, refresh_page, data):
        """添加文件后缀名过滤测试,直接保存"""
        suffix_page = login[4]
        suffix_page.add_suffix_directSave()
        result = suffix_page.add_suffix_exception_text()
        assert data["expected"] in result, "添加失败， 断言失败"


    @pytest.mark.parametrize("data", suffix_data.delete_suffix_noSelect_data, ids=delete_suffix_noSelect_ids)
    def test_delete_suffix_noSelect(self, login, refresh_page, data):
        """删除文件后缀名过滤测试,不选择列表"""
        suffix_page = login[4]
        suffix_page.delete_suffix_noSelect()
        result = suffix_page.add_suffix_exception_text()
        assert data["expected"] in result, "删除失败， 断言失败"

    @pytest.mark.parametrize("data", suffix_data.delete_suffix_single_data, ids=delete_suffix_single_ids)
    def test_delete_suffix_single(self, login, refresh_page, data):
        """删除文件后缀名过滤测试,单选未被任务使用"""
        suffix_page = login[4]
        suffix_page.delete_suffix_single()
        result = suffix_page.add_suffix_text()
        assert data["expected"] in result, "删除成功， 断言成功"

    @pytest.mark.xfail(condition=2 > 1, reason="未建立任务")
    @pytest.mark.parametrize("data", suffix_data.delete_suffix_employ_data, ids=delete_suffix_employ_ids)
    def test_delete_suffix_singleEmploy(self, login, refresh_page, data):
        """删除文件后缀名过滤测试,单选被任务使用"""
        suffix_page = login[4]
        suffix_page.delete_suffix_singleEmploy()
        result = suffix_page.add_suffix_text()
        assert data["expected"] in result, "删除失败， 断言失败"

    @pytest.mark.parametrize("data", suffix_data.delete_suffix_multipleChoice_data, ids=delete_suffix_multipleChoice_ids)
    def test_delete_suffix_multipleChoice(self, login, refresh_page, data):
        """删除文件后缀名过滤测试,多选删除"""
        suffix_page = login[4]
        suffix_page.delete_suffix_multipleChoice()
        result = suffix_page.add_suffix_text()
        assert data["expected"] in result, "删除成功， 断言成功"

    @pytest.mark.parametrize("data", suffix_data.delete_suffix_allSelect_data, ids=delete_suffix_allSelect_ids)
    def test_delete_suffix_allSelect(self, login, refresh_page, data):
        """删除文件后缀名过滤测试,全选"""
        suffix_page = login[4]
        suffix_page.delete_suffix_allSelect()
        result = suffix_page.add_suffix_text()
        assert data["expected"] in result, "删除成功， 断言失败"


if __name__ == "__main__":
    pytest.main()

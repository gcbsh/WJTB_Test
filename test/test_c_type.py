import pytest
from data.type_data import TypeData

# 改变输出结果
create_type_ids = [
    "测试：{}->[预期:{}]".
        format(data["case"],  data["expected"]) for data in TypeData.create_type_data
]
create_type_chineseName_ids = [
    "测试：{}->[预期:{}]".
        format(data["case"],  data["expected"]) for data in TypeData.create_type_chineseName_data
]
create_type_EnglishName_ids = [
    "测试：{}->[预期:{}]".
        format(data["case"],  data["expected"]) for data in TypeData.create_type_EnglishName_data
]
create_type_englishName_ids = [
    "测试：{}->[预期:{}]".
        format(data["case"],  data["expected"]) for data in TypeData.create_type_englishName_data
]
create_type_numberName_ids = [
    "测试：{}->[预期:{}]".
        format(data["case"],  data["expected"]) for data in TypeData.create_type_numberName_data
]
create_type_halfSymbolName_ids = [
    "测试：{}->[预期:{}]".
        format(data["case"],  data["expected"]) for data in TypeData.create_type_halfSymbolName_data
]
create_type_entireSymbolName_ids = [
    "测试：{}->[预期:{}]".
        format(data["case"],  data["expected"]) for data in TypeData.create_type_entireSymbolName_data
]
create_type_superLongName33_ids = [
    "测试：{}->[预期:{}]".
        format(data["case"],  data["expected"]) for data in TypeData.create_type_superLongName33_data
]
create_type_superLongName32_ids = [
    "测试：{}->[预期:{}]".
        format(data["case"],  data["expected"]) for data in TypeData.create_type_superLongName32_data
]
name_none_ids = [
    "测试：{}->[预期:{}]".
        format(data["case"],  data["expected"]) for data in TypeData.name_none_data
]
name_halfSpace_ids = [
    "测试：{}->[预期:{}]".
        format(data["case"],  data["expected"]) for data in TypeData.name_halfSpace_data
]
name_entireSpace_ids = [
    "测试：{}->[预期:{}]".
        format(data["case"],  data["expected"]) for data in TypeData.name_entireSpace_data
]
create_type_sameName_ids = [
    "测试：{}->[预期:{}]".
        format(data["case"],  data["expected"]) for data in TypeData.create_type_sameName_data
]
create_type_directSave_ids = [
    "测试：{}->[预期:{}]".
        format(data["case"],  data["expected"]) for data in TypeData.create_type_directSave_data
]
file_none_ids = [
    "测试：{}->[预期:{}]".
        format(data["case"],  data["expected"]) for data in TypeData.file_none_data
]
fileCode_none_ids = [
    "测试：{}->[预期:{}]".
        format(data["case"],  data["expected"]) for data in TypeData.fileCode_none_data
]
create_type_samefile_ids = [
    "测试：{}->[预期:{}]".
        format(data["case"],  data["expected"]) for data in TypeData.create_type_samefile_data
]
create_type_renameFile_ids = [
    "测试：{}->[预期:{}]".
        format(data["case"],  data["expected"]) for data in TypeData.create_type_renameFile_data
]
create_type_sameFilename_ids = [
    "测试：{}->[预期:{}]".
        format(data["case"],  data["expected"]) for data in TypeData.create_type_sameFilename_data
]
cancel_type_ids = [
    "测试：{}->[预期:{}]".
        format(data["case"],  data["expected"]) for data in TypeData.cancel_type_data
]
search_type_Chinese_ids = [
    "测试：{}->[预期:{}]".
        format(data["case"],  data["expected"]) for data in TypeData.search_type_Chinese_data
]
search_type_english_ids = [
    "测试：{}->[预期:{}]".
        format(data["case"],  data["expected"]) for data in TypeData.search_type_english_data
]
search_type_English_ids = [
    "测试：{}->[预期:{}]".
        format(data["case"],  data["expected"]) for data in TypeData.search_type_English_data
]
search_type_number_ids = [
    "测试：{}->[预期:{}]".
        format(data["case"],  data["expected"]) for data in TypeData.search_type_number_data
]
search_type_halfSymbol_ids = [
    "测试：{}->[预期:{}]".
        format(data["case"],  data["expected"]) for data in TypeData.search_type_halfSymbol_data
]
search_type_entireSymbol_ids = [
    "测试：{}->[预期:{}]".
        format(data["case"],  data["expected"]) for data in TypeData.search_type_entireSymbol_data
]
delete_type_single_ids = [
    "测试：{}->[预期:{}]".
        format(data["case"],  data["expected"]) for data in TypeData.delete_type_single_data
]
delete_type_noSelect_ids = [
    "测试：{}->[预期:{}]".
        format(data["case"],  data["expected"]) for data in TypeData.delete_type_noSelect_data
]
delete_type_allSelect_ids = [
    "测试：{}->[预期:{}]".
        format(data["case"],  data["expected"]) for data in TypeData.delete_type_allSelect_data
]
delete_type_employ_ids = [
    "测试：{}->[预期:{}]".
        format(data["case"],  data["expected"]) for data in TypeData.delete_type_employ_data
]
delete_type_multipleChoice_ids = [
    "测试：{}->[预期:{}]".
        format(data["case"],  data["expected"]) for data in TypeData.delete_type_multipleChoice_data
]
#导入添加文件类型数据
route_name = TypeData.test_file_type_data

@pytest.mark.loginTest
class Test_Type(object):
    """文件类型管理测试"""
    type_data = TypeData

    @pytest.mark.parametrize("data", type_data.cancel_type_data, ids=cancel_type_ids)
    def test_create_type_cancel(self, login,refresh_page, data):
        """创建文件类型管理测试,取消"""
        type_page = login[3]
        type_page.add_type_process_cancel()
        result = type_page.cancel_type_text()
        assert data["expected"] in result, "创建失败， 断言失败"

    @pytest.mark.parametrize("data", type_data.create_type_chineseName_data, ids=create_type_chineseName_ids)
    def test_create_type_ChineseName(self, login,refresh_page, data):
        """创建文件类型管理测试,中文名称"""
        type_page = login[3]
        type_page.add_type_process(route_name[1][0],route_name[1][1])
        result = type_page.save_type_text()
        assert data["expected"] in result, "创建成功， 断言成功"

    @pytest.mark.parametrize("data", type_data.create_type_EnglishName_data, ids=create_type_EnglishName_ids)
    def test_create_type_EnglishName(self, login,refresh_page, data):
        """创建文件类型管理测试,名称英文大写"""
        type_page = login[3]
        type_page.add_type_process(route_name[2][0],route_name[2][1])
        result = type_page.save_type_text()
        assert data["expected"] in result, "创建成功， 断言成功"

    @pytest.mark.parametrize("data", type_data.create_type_englishName_data, ids=create_type_englishName_ids)
    def test_create_type_englishName(self, login,refresh_page, data):
        """创建文件类型管理测试,名称英文小写"""
        type_page = login[3]
        type_page.add_type_process(route_name[3][0],route_name[3][1])
        result = type_page.save_type_text()
        assert data["expected"] in result, "创建成功， 断言成功"

    @pytest.mark.parametrize("data", type_data.create_type_numberName_data, ids=create_type_numberName_ids)
    def test_create_type_numberName(self, login,refresh_page, data):
        """创建文件类型管理测试,名称数字"""
        type_page = login[3]
        type_page.add_type_process(route_name[4][0],route_name[4][1])
        result = type_page.save_type_text()
        assert data["expected"] in result, "创建成功， 断言成功"

    @pytest.mark.parametrize("data", type_data.create_type_halfSymbolName_data, ids=create_type_halfSymbolName_ids)
    def test_create_type_halfSymbolName(self, login,refresh_page, data):
        """创建文件类型管理测试,名称半角符号"""
        type_page = login[3]
        type_page.add_type_process(route_name[5][0],route_name[5][1])
        result = type_page.save_type_text()
        assert data["expected"] in result, "创建成功， 断言成功"

    @pytest.mark.parametrize("data", type_data.create_type_entireSymbolName_data, ids=create_type_entireSymbolName_ids)
    def test_create_type_entireSymbolName(self, login,refresh_page, data):
        """创建文件类型管理测试,名称全角符号"""
        type_page = login[3]
        type_page.add_type_process(route_name[6][0],route_name[6][1])
        result = type_page.save_type_text()
        assert data["expected"] in result, "创建成功， 断言成功"

    @pytest.mark.parametrize("data", type_data.create_type_superLongName33_data, ids=create_type_superLongName33_ids)
    def test_create_type_superLongName33(self,login,refresh_page,data):
        """创建文件类型管理测试,名称超长字符33位"""
        type_page = login[3]
        type_page.add_type_process_superLongName(route_name[7][0], route_name[7][1])
        result = type_page.Tips_text()
        assert data["expected"] in result, "创建失败， 断言成功"

    @pytest.mark.parametrize("data", type_data.create_type_superLongName32_data, ids=create_type_superLongName32_ids)
    def test_create_type_superLongName32(self, login,refresh_page, data):
        """创建文件类型管理测试,名称超长字符32位"""
        type_page = login[3]
        type_page.add_type_process_superLongName(route_name[8][0], route_name[8][1])
        result = type_page.save_type_text()
        assert data["expected"] in result, "创建成功， 断言成功"

    @pytest.mark.parametrize("data", type_data.name_none_data, ids=name_none_ids)
    def test_create_type_noneName(self, login,refresh_page, data):
        """创建文件类型管理测试,名称为空"""
        type_page = login[3]
        type_page.add_type_process_noneName(route_name[0][0])
        result = type_page.Tips_text()
        assert data["expected"] in result, "创建失败， 断言失败"

    @pytest.mark.parametrize("data", type_data.name_halfSpace_data, ids=name_halfSpace_ids)
    def test_create_type_halfSpaceName(self, login,refresh_page, data):
        """创建文件类型管理测试,名称为半角空格"""
        type_page = login[3]
        type_page.add_type_process_spaceName(route_name[0][0]," ")
        result = type_page.Tips_text()
        assert data["expected"] in result, "创建失败， 断言失败"

    @pytest.mark.parametrize("data", type_data.create_type_renameFile_data, ids=create_type_renameFile_ids)
    def test_create_type_renameFile(self, login, refresh_page, data):
        """创建文件类型管理测试,同一文件但文件名不同"""
        type_page = login[3]
        type_page.add_type_process(route_name[9][0], route_name[9][1])
        result = type_page.save_type_text()
        assert data["expected"] in result, "创建失败， 断言失败"


    @pytest.mark.xfail(condition=2>1,reason='提示信息不够准确')
    @pytest.mark.parametrize("data", type_data.create_type_sameName_data, ids=create_type_sameName_ids)
    def test_create_type_sameName(self, login,refresh_page, data):
        """创建文件类型管理测试,相同名称但类型不同"""
        type_page = login[3]
        type_page.add_type_process(route_name[10][0],route_name[10][1])
        result = type_page.save_type_text()
        assert data["expected"] in result, "创建失败， 断言失败"

    @pytest.mark.parametrize("data", type_data.name_entireSpace_data, ids=name_entireSpace_ids)
    def test_create_type_entireSpaceName(self, login,refresh_page, data):
        """创建文件类型管理测试,名称为全角空格"""
        type_page = login[3]
        type_page.add_type_process_spaceName(route_name[0][0],"　")
        result = type_page.Tips_text()
        assert data["expected"] in result, "创建失败， 断言失败"

    @pytest.mark.parametrize("data", type_data.create_type_directSave_data, ids=create_type_directSave_ids)
    def test_create_type_directSave(self, login,refresh_page, data):
        """创建文件类型管理测试,直接保存"""
        type_page = login[3]
        type_page.add_type_process_directSave()
        result = type_page.Tips_text()
        assert data["expected"] in result, "创建失败， 断言失败"

    @pytest.mark.parametrize("data", type_data.file_none_data, ids=file_none_ids)
    def test_create_type_noneFile(self, login,refresh_page, data):
        """创建文件类型管理测试,不选择文件保存"""
        type_page = login[3]
        type_page.add_type_process_nonefile(route_name[0][1])
        result = type_page.save_type_text()
        assert data["expected"] in result, "创建失败， 断言失败"

    @pytest.mark.parametrize("data", type_data.fileCode_none_data, ids=fileCode_none_ids)
    def test_create_type_noneFileCode(self, login,refresh_page, data):
        """创建文件类型管理测试,选择文件不生成特征码保存"""
        type_page = login[3]
        type_page.add_type_process_nonefileCode(route_name[0][0],route_name[0][1])
        result = type_page.save_type_text()
        assert data["expected"] in result, "创建失败， 断言失败"

    @pytest.mark.parametrize("data", type_data.create_type_samefile_data, ids=create_type_samefile_ids)
    def test_create_type_samefile(self, login, refresh_page, data):
        """创建文件类型管理测试,相同文件但名称不同"""
        type_page = login[3]
        type_page.add_type_process(route_name[1][0], route_name[0][1])
        result = type_page.save_type_text()
        assert data["expected"] in result, "创建失败， 断言失败"


    @pytest.mark.parametrize("data", type_data.create_type_sameFilename_data, ids=create_type_sameFilename_ids)
    def test_create_type_sameFilename(self, login, refresh_page, data):
        """创建文件类型管理测试,不同类型文件但文件名相同"""
        type_page = login[3]
        type_page.add_type_process(route_name[11][0], route_name[11][1])
        result = type_page.save_type_text()
        assert data["expected"] in result, "创建失败， 断言失败"

    @pytest.mark.parametrize("data", type_data.search_type_Chinese_data, ids=search_type_Chinese_ids)
    def test_search_type_Chinese(self, login, refresh_page, data):
        """搜索文件类型管理测试,中文搜索"""
        type_page = login[3]
        type_page.search_type_process(route_name[1][1])
        result = type_page.search_type_text()
        assert data["expected"] in result, "搜索成功， 断言成功"

    @pytest.mark.parametrize("data", type_data.search_type_English_data, ids=search_type_English_ids)
    def test_search_type_English(self, login, refresh_page, data):
        """搜索文件类型管理测试,英文大写搜索"""
        type_page = login[3]
        type_page.search_type_process(route_name[2][1])
        result = type_page.search_type_text()
        assert data["expected"] in result, "搜索成功， 断言成功"

    @pytest.mark.parametrize("data", type_data.search_type_english_data, ids=search_type_english_ids)
    def test_search_type_english(self, login, refresh_page, data):
        """搜索文件类型管理测试,英文小写搜索"""
        type_page = login[3]
        type_page.search_type_process(route_name[3][1])
        result = type_page.search_type_text()
        assert data["expected"] in result, "搜索成功， 断言成功"

    @pytest.mark.parametrize("data", type_data.search_type_number_data, ids=search_type_number_ids)
    def test_search_type_number(self, login, refresh_page, data):
        """搜索文件类型管理测试,数字搜索"""
        type_page = login[3]
        type_page.search_type_process(route_name[4][1])
        result = type_page.search_type_text()
        assert data["expected"] in result, "搜索成功， 断言成功"

    @pytest.mark.parametrize("data", type_data.search_type_halfSymbol_data, ids=search_type_halfSymbol_ids)
    def test_search_type_halfSymbol(self, login, refresh_page, data):
        """搜索文件类型管理测试,半角符号搜索"""
        type_page = login[3]
        type_page.search_type_process(route_name[5][1])
        result = type_page.search_type_text()
        assert data["expected"] in result, "搜索成功， 断言成功"

    @pytest.mark.parametrize("data", type_data.search_type_entireSymbol_data, ids=search_type_entireSymbol_ids)
    def test_search_type_entireSymbol(self, login, refresh_page, data):
        """搜索文件类型管理测试,全角符号搜索"""
        type_page = login[3]
        type_page.search_type_process(route_name[6][1])
        result = type_page.search_type_text()
        assert data["expected"] in result, "搜索成功， 断言成功"

    @pytest.mark.parametrize("data", type_data.delete_type_noSelect_data, ids=delete_type_noSelect_ids)
    def test_delete_type_noSelect(self, login, refresh_page, data):
        """删除文件类型管理测试,不选择列表"""
        type_page = login[3]
        type_page.delete_type_noSelect()
        result = type_page.Tips_text()
        assert data["expected"] in result, "创建失败， 断言失败"

    @pytest.mark.parametrize("data", type_data.delete_type_single_data, ids=delete_type_single_ids)
    def test_delete_type_single(self, login,refresh_page, data):
        """删除文件类型管理测试,单选删除,没有被任务使用"""
        type_page = login[3]
        type_page.delete_type_single()
        result = type_page.save_type_text()
        assert data["expected"] in result, "创建失败， 断言失败"

    @pytest.mark.xfail(condition=2>1,reason="任务未建立")
    @pytest.mark.parametrize("data", type_data.delete_type_employ_data, ids=delete_type_employ_ids)
    def test_delete_type_singleEmploy(self, login,refresh_page, data):
        """删除文件类型管理测试,单选删除被任务使用"""
        type_page = login[3]
        type_page.delete_type_singleEmploy()
        result = type_page.save_type_text()
        assert data["expected"] in result, "创建失败， 断言失败"

    @pytest.mark.parametrize("data", type_data.delete_type_multipleChoice_data, ids=delete_type_multipleChoice_ids)
    def test_delete_type_multipleChoice(self, login,refresh_page, data):
        """删除文件类型管理测试,多选删除"""
        type_page = login[3]
        type_page.delete_type_multipleChoice()
        result = type_page.save_type_text()
        assert data["expected"] in result, "创建失败， 断言失败"

    @pytest.mark.parametrize("data", type_data.delete_type_allSelect_data, ids=delete_type_allSelect_ids)
    def test_delete_type_allSelect(self, login,refresh_page, data):
        """删除文件类型管理测试,全选删除"""
        type_page = login[3]
        type_page.delete_type_allSelect()
        result = type_page.save_type_text()
        assert data["expected"] in result, "创建失败， 断言失败"

if __name__ == "__main__":
    pytest.main()


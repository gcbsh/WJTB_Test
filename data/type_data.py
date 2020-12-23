class TypeData(object):
    """创建文件类型管理测试数据"""

    create_type_data = [
        {
            "case": "创建文件类型管理测试,循环添加常用类型",
            "expected": "添加成功",
        }
    ]
    create_type_chineseName_data = [
        {
            "case": "创建文件类型管理测试,中文名称",
            "expected": "添加成功",
        }
    ]
    create_type_EnglishName_data = [
        {
            "case": "创建文件类型管理测试,名称英文大写",
            "expected": "添加成功",
        }
    ]
    create_type_englishName_data = [
        {
            "case": "创建文件类型管理测试,名称英文小写",
            "expected": "添加成功",
        }
    ]
    create_type_numberName_data = [
        {
            "case": "创建文件类型管理测试,名称数字",
            "expected": "添加成功",
        }
    ]
    create_type_halfSymbolName_data = [
        {
            "case": "创建文件类型管理测试,名称半角字符",
            "expected": "添加成功",
        }
    ]
    create_type_entireSymbolName_data = [
        {
            "case": "创建文件类型管理测试,名称全角字符",
            "expected": "添加成功",
        }
    ]
    create_type_superLongName33_data = [
        {
            "case": "创建文件类型管理测试,名称超长字符33位",
            "expected": "类型名称长度不能超过32位",
        }
    ]
    create_type_superLongName32_data = [
        {
            "case": "创建文件类型管理测试,名称超长字符32位",
            "expected": "添加成功",
        }
    ]
    create_type_pasteName_data = [
            {
                "case": "创建文件类型管理测试,名称32位字符",
                "expected": "添加成功",
            }
    ]
    name_none_data = [
        {
            "case": "创建文件类型管理测试,名称为空",
            "expected": "类型名称不能为空",
        }
    ]
    name_halfSpace_data = [
        {
            "case": "创建文件类型管理测试,名称为半角空格",
            "expected": "类型名称中不能全为空格",
        }
    ]
    name_entireSpace_data = [
        {
            "case": "创建文件类型管理测试,名称为全角空格",
            "expected": "类型名称中不能全为空格",
        }
    ]
    create_type_sameName_data = [
        {
            "case": "创建文件类型管理测试,相同名称但类型不同",
            "expected": "文件类型名称已存在",
        }
    ]
    create_type_directSave_data = [
        {
            "case": "创建文件类型管理测试,直接保存",
            "expected": "类型名称不能为空",
        }
    ]
    file_none_data = [
        {
            "case": "创建文件类型管理测试,不选择文件保存",
            "expected": "样本文件名不能为空",
        }
    ]
    fileCode_none_data = [
        {
            "case": "创建文件类型管理测试,选择文件不生成特征码保存",
            "expected": "样本文件名不能为空",
        }
    ]
    create_type_samefile_data = [
        {
            "case": "创建文件类型管理测试,相同文件但名称不同",
            "expected": "文件特征串已存在",
        }
    ]
    create_type_renameFile_data = [
        {
            "case": "创建文件类型管理测试,同一文件但文件名不同",
            "expected": "文件特征串已存在",
        }
    ]
    create_type_sameFilename_data = [
        {
            "case": "创建文件类型管理测试,不同类型文件但文件名相同",
            "expected": "添加成功",
        }
    ]
    cancel_type_data = [
        {
            "case": "创建文件类型管理测试,取消",
            "expected": "ID",
        }
    ]
    search_type_Chinese_data = [
        {
            "case": "搜索文件类型管理测试,中文搜索",
            "expected": "(1)安卓",
        }
    ]
    search_type_English_data = [
        {
            "case": "搜索文件类型管理测试,英文小写搜索",
            "expected": "(2)DOC",
        }
    ]
    search_type_english_data = [
        {
            "case": "搜索文件类型管理测试,英文大写搜索",
            "expected": "(3)docx",
        }
    ]
    search_type_number_data = [
        {
            "case": "搜索文件类型管理测试,数字",
            "expected": "(4)1234567890",
        }
    ]
    search_type_halfSymbol_data = [
        {
            "case": "搜索文件类型管理测试,半角符号搜索",
            "expected": "(5)!@#$%*",
        }
    ]
    search_type_entireSymbol_data = [
        {
            "case": "搜索文件类型管理测试,全角符号搜索",
            "expected": "(6)！＠＃＄％＊",
        }
    ]
    delete_type_noSelect_data = [
        {
            "case": "删除文件类型管理测试,不选择列表",
            "expected": "请至少选择一条记录删除",
        }
    ]
    delete_type_single_data = [
        {
            "case": "删除文件类型管理测试,单选删除,没有被任务使用",
            "expected": "删除成功",
        }
    ]
    delete_type_employ_data = [
        {
            "case": "删除文件类型管理测试,单选删除被任务使用",
            "expected": "文件类型正在被任务使用",
        }
    ]
    delete_type_multipleChoice_data = [
        {
            "case": "删除文件类型管理测试,多选删除",
            "expected": "删除成功",
        }
    ]
    delete_type_allSelect_data = [
        {
            "case": "删除文件类型管理测试,全选",
            "expected": "删除成功",
        }
    ]
    test_file_type_data = (
        (
            "F:\测试物料\各种后缀名文件\png.png",
            "(0)png"
        ),
        (
            r"F:\测试物料\各种后缀名文件\apk.apk",
            "(1)安卓"
        ),
        (
            "F:\测试物料\各种后缀名文件\doc.doc",
            "(2)DOC"
        ),
        (
            "F:\测试物料\各种后缀名文件\docx.docx",
            "(3)docx"
        ),
        (
            "F:\测试物料\各种后缀名文件\exe.exe",
            "(4)1234567890"
        ),
        (
            r"F:\测试物料\各种后缀名文件\gif.gif",
            "(5)!@#$%*"
        ),
        (
            "F:\测试物料\各种后缀名文件\gz.gz",
            "(6)！＠＃＄％＊"
        ),
        (
            "F:\测试物料\各种后缀名文件\html.html",
            "(7)000000000000000000000000000000"
        ),
        (
            r"F:\测试物料\各种后缀名文件\bat.bat",
            "(8)00000000000000000000000000000"
        ),
        (
            r"F:\测试物料\各种后缀名文件\apk - 副本.apk",
            "(9)"
        ),
        (
            r"F:\测试物料\各种后缀名文件\png.png",
            "(8)00000000000000000000000000000"
        ),
        (
            r"F:\测试物料\各种后缀名文件\txt\apk.apk",
            "(11)"
        ),
    )

if __name__ == '__main__':
    pass

class SuffixData(object):
    """添加文件后缀名测试数据"""
    test_suffix_data = (
        "中文","EXE","exe","123","!@#$%^&","！＠＃＄％＾＆＊",
        "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    )
    add_suffix_Chinese_data = [
        {
            "case": "添加文件后缀名过滤测试,中文后缀",
            "expected": "后缀名不能包含中文",
        }
    ]
    add_suffix_English_data = [
        {
            "case": "添加文件后缀名过滤测试,英文大写后缀",
            "expected": "字母不能为大写",
        }
    ]
    add_suffix_english_data = [
        {
            "case": "添加文件后缀名过滤测试,英文小写后缀",
            "expected": "添加成功",
        }
    ]
    add_suffix_number_data = [
        {
            "case": "添加文件后缀名过滤测试,数字后缀",
            "expected": "添加成功",
        }
    ]
    add_suffix_halfSymbol_data = [
        {
            "case": "添加文件后缀名过滤测试,半角符号后缀",
            "expected": "添加成功",
        }
    ]
    add_suffix_entireSymbol_data = [
        {
            "case": "添加文件后缀名过滤测试,全角符号后缀",
            "expected": "添加成功",
        }
    ]
    add_suffix_superLong64_data = [
        {
            "case": "添加文件后缀名过滤测试,超长后缀64位字符",
            "expected": "添加成功",
        }
    ]
    add_suffix_superLong65_data = [
        {
            "case": "添加文件后缀名过滤测试,超长后缀65位字符",
            "expected": "后缀名不能超过64个字符",
        }
    ]
    search_suffix_English_data = [
        {
            "case": "搜索文件后缀名过滤测试,英文搜索(不区分大小写)",
            "expected": "exe",
        }
    ]
    search_suffix_number_data = [
        {
            "case": "搜索文件后缀名过滤测试,数字搜索",
            "expected": "123",
        }
    ]
    search_suffix_halfSymbol_data = [
        {
            "case": "搜索文件后缀名过滤测试,半角字符搜索",
            "expected": "!@#$%^&",
        }
    ]
    search_suffix_entireSymbol_data = [
        {
            "case": "搜索文件后缀名过滤测试,全角字符搜索",
            "expected": "！＠＃＄％＾＆＊",
        }
    ]


    none_suffix_data = [
        {
            "case":"添加文件后缀名过滤测试,直接保存",
            "expected":"后缀名不能为空",
        }
    ]
    cancel_suffix_data = [
        {
            "case": "添加文件后缀名过滤测试,取消",
            "expected": "ID",
        }
    ]
    delete_suffix_noSelect_data = [
        {
            "case": "删除文件后缀名过滤测试,不选择列表",
            "expected": "请至少选择一条数据删除",
        }
    ]
    delete_suffix_single_data = [
        {
            "case": "删除文件后缀名过滤测试,单选未被任务使用",
            "expected": "删除成功",
        }
    ]
    delete_suffix_employ_data = [
        {
            "case": "删除文件后缀名过滤测试,单选被任务使用",
            "expected": "正在被任务使用",
        }
    ]
    delete_suffix_multipleChoice_data = [
        {
            "case": "删除文件后缀名过滤测试,多选删除",
            "expected": "删除成功",
        }
    ]
    delete_suffix_allSelect_data = [
        {
            "case": "删除文件后缀名过滤测试,全选",
            "expected": "删除成功",
        }
    ]


if __name__ == '__main__':
    pass

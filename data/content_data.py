class ContentData(object):
    """添加文件内容过滤测试数据"""

    test_content_data = (
        "我爱中国",
        "ABCDEFG",
        "hijklmn",
        "1234567890",
        "!@#$%^&",
        "～！＠＃＄％＾＆＊",
        " ",
        "　",
        "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    )
    add_content_none_data = [
        {
            "case": "添加文件内容过滤测试,为空(直接保存)",
            "expected": "过滤内容不能为空",
        }
    ]
    add_content_cancel_data = [
        {
            "case": "添加文件内容过滤测试,取消",
            "expected": "ID",
        }
    ]
    add_content_Chinese_data = [
        {
            "case": "添加文件内容过滤测试,中文",
            "expected": "添加成功",
        }
    ]
    add_content_English_data = [
        {
            "case": "添加文件内容过滤测试,英文大写",
            "expected": "添加成功",
        }
    ]
    add_content_english_data = [
        {
            "case": "添加文件内容过滤测试,英文小写",
            "expected": "添加成功",
        }
    ]
    add_content_number_data = [
        {
            "case": "添加文件内容过滤测试,数字",
            "expected": "添加成功",
        }
    ]
    add_content_halfSymbol_data = [
        {
            "case": "添加文件内容过滤测试,半角符号",
            "expected": "添加成功",
        }
    ]
    add_content_entireSymbol_data = [
        {
            "case": "添加文件内容过滤测试,全角符号",
            "expected": "添加成功",
        }
    ]
    add_content_halfSpace_data = [
        {
            "case": "添加文件内容过滤测试,仅有半角空格",
            "expected": "过滤内容不能全为空格",
        }
    ]
    add_content_entireSpace_data = [
        {
            "case": "添加文件内容过滤测试,仅有全角空格",
            "expected": "过滤内容不能全为空格",
        }
    ]
    add_content_superLong64_data = [
        {
            "case": "添加文件内容过滤测试,超长字符64位",
            "expected": "添加成功",
        }
    ]
    add_content_superLong65_data = [
        {
            "case": "添加文件内容过滤测试,超长字符64位",
            "expected": "过滤内容最多只能输入64位字符或21个汉字",
        }
    ]
    search_content_chinese_data = [
        {
            "case": "搜索文件内容过滤测试,中文搜索",
            "expected": "我爱中国",
        }
    ]
    search_content_English_data = [
        {
            "case": "搜索文件内容过滤测试,英文大写搜索",
            "expected": "ABCDEFG",
        }
    ]
    search_content_english_data = [
        {
            "case": "搜索文件内容过滤测试,英文小写搜索",
            "expected": "hijklmn",
        }
    ]
    search_content_number_data = [
        {
            "case": "搜索文件内容过滤测试,英文小写搜索",
            "expected": "1234567890",
        }
    ]
    search_content_halfSymbol_data = [
        {
            "case": "搜索文件内容过滤测试,半角符号搜索",
            "expected": "!@#$%^&",
        }
    ]
    search_content_entireSymbol_data = [
        {
            "case": "搜索文件内容过滤测试,全角符号搜索",
            "expected": "！＠＃＄％＾＆＊",
        }
    ]
    delete_content_noSelect_data = [
        {
            "case": "删除文件内容过滤测试,不选择列表",
            "expected": "请至少选择一条数据删除",
        }
    ]
    delete_content_single_data = [
        {
            "case": "删除文件内容过滤测试,单选未被任务使用",
            "expected": "删除成功",
        }
    ]
    delete_content_singleEmploy_data = [
        {
            "case": "删除文件内容过滤测试,单选被任务使用",
            "expected": "被任务使用",
        }
    ]
    delete_content_multipleChoice_data = [
        {
            "case": "删除文件内容过滤测试,多选",
            "expected": "删除成功",
        }
    ]
    delete_content_allSelect_data = [
        {
            "case": "删除文件内容过滤测试,全选",
            "expected": "删除成功",
        }
    ]


if __name__ == '__main__':
    pass

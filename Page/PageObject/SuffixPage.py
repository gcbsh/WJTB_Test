from Page.BasePage import BasePage
from util.parseConFile import ParseConFile


class SuffixPage(BasePage):
    # 配置文件读取元素
    do_conf = ParseConFile()
    # 文件同步模块按钮
    loginText = do_conf.get_locators_or_account('HomePageElements', 'loginText')
    # 文件后缀名管理按钮
    suffixBtn = do_conf.get_locators_or_account('SuffixPageElements', 'suffixBtn')
    # 添加后缀名按钮
    add_suffixBtn = do_conf.get_locators_or_account('SuffixPageElements', 'add_suffixBtn')
    # 后缀名名称输入框
    suffixBox = do_conf.get_locators_or_account('SuffixPageElements', 'suffixBox')
    # 保存后缀名按钮
    save_suffixBtn = do_conf.get_locators_or_account('SuffixPageElements', 'save_suffixBtn')
    # 保存成功的验证信息
    save_suffixText = do_conf.get_locators_or_account('SuffixPageElements', 'save_suffixText')
    # 失败/成功,确认按钮
    qdBtn = do_conf.get_locators_or_account('SharedPageElements', 'qdBtn')
    # 文件后缀名错误验证信息
    name_noneText = do_conf.get_locators_or_account('TypePageElements', 'name_noneText')
    # 取消按钮
    cancelBtn = do_conf.get_locators_or_account('SuffixPageElements', 'cancelBtn')
    # 取消成功验证信息
    cancel_suffixText = do_conf.get_locators_or_account('SuffixPageElements', 'cancel_suffixText')
    # 搜索输入框
    search_suffix = do_conf.get_locators_or_account('SuffixPageElements', 'search_suffix')
    # 搜索验证信息
    search_suffixText = do_conf.get_locators_or_account('SuffixPageElements', 'search_suffixText')
    # 文件后缀名列表复选框按钮, 全选和按照顺序选
    all_selectBtn = do_conf.get_locators_or_account('SuffixPageElements', 'all_selectBtn')
    select_suffixBtn1 = do_conf.get_locators_or_account('SuffixPageElements', 'select_suffixBtn1')
    select_suffixBtn2 = do_conf.get_locators_or_account('SuffixPageElements', 'select_suffixBtn2')
    select_suffixBtn3 = do_conf.get_locators_or_account('SuffixPageElements', 'select_suffixBtn3')

    # 删除按钮
    deleteBtn = do_conf.get_locators_or_account('SuffixPageElements', 'deleteBtn')

    # 进入后缀名过滤页面
    def add_suffix(self):
        self.sleep(0.5)
        self.click(*SuffixPage.loginText)
        self.sleep(1)
        self.click(*SuffixPage.suffixBtn)
        self.sleep(1)
        iframe = self.driver.find_element_by_tag_name('iframe')
        self.driver.switch_to_frame(iframe)

    # 添加后缀名流程
    def add_suffix_process(self,suffixName):
        self.add_suffix()
        self.click(*SuffixPage.add_suffixBtn)
        self.sleep(1)
        self.find_element(*SuffixPage.suffixBox).send_keys(suffixName)
        self.sleep(0.5)
        self.click(*SuffixPage.save_suffixBtn)
        self.sleep(1)

    # 添加后缀名,直接保存
    def add_suffix_directSave(self):
        self.add_suffix()
        self.sleep(1)
        self.click(*SuffixPage.add_suffixBtn)
        self.sleep(0.5)
        self.click(*SuffixPage.save_suffixBtn)
        self.sleep(1)
    # 添加后缀名,取消
    def add_suffix_cancel(self):
        self.add_suffix()
        self.sleep(1)
        self.click(*SuffixPage.add_suffixBtn)
        self.sleep(0.5)
        self.click(*SuffixPage.cancelBtn)
        self.sleep(1)

    #搜索后缀名流程
    def search_suffix_process(self,searchData):
        self.add_suffix()
        self.find_element(*SuffixPage.search_suffix).send_keys(searchData)
        self.sleep(1)

    # 删除后缀名,不选择列表
    def delete_suffix_noSelect(self):
        self.add_suffix()
        self.sleep(0.5)
        self.click(*SuffixPage.deleteBtn)
        self.sleep(1)

    # 删除后缀名,单选未被任务使用的
    def delete_suffix_single(self):
        self.add_suffix()
        self.sleep(0.5)
        self.click(*SuffixPage.select_suffixBtn2)
        self.sleep(0.5)
        self.click(*SuffixPage.deleteBtn)
        self.sleep(0.5)
        self.click(*SuffixPage.qdBtn)
        self.sleep(1)


    # 删除后缀名,单选被任务使用的
    def delete_suffix_singleEmploy(self):
        self.add_suffix()
        self.sleep(0.5)
        self.click(*SuffixPage.select_suffixBtn1)
        self.sleep(0.5)
        self.click(*SuffixPage.deleteBtn)
        self.sleep(0.5)
        self.click(*SuffixPage.qdBtn)
        self.sleep(1)


    # 删除后缀名,多选删除
    def delete_suffix_multipleChoice(self):
        self.add_suffix()
        self.sleep(0.5)
        self.click(*SuffixPage.select_suffixBtn2)
        self.click(*SuffixPage.select_suffixBtn3)
        self.sleep(0.5)
        self.click(*SuffixPage.deleteBtn)
        self.sleep(0.5)
        self.click(*SuffixPage.qdBtn)
        self.sleep(1)

    # 删除后缀名,全选
    def delete_suffix_allSelect(self):
        self.add_suffix()
        self.sleep(0.5)
        self.click(*SuffixPage.all_selectBtn)
        self.sleep(0.5)
        self.click(*SuffixPage.deleteBtn)
        self.sleep(0.5)
        self.click(*SuffixPage.qdBtn)
        self.sleep(1)

    # 后缀名添加成功的验证信息
    def add_suffix_text(self):
        return self.get_element_text(*SuffixPage.save_suffixText)
    # 后缀名异常验证信息
    def add_suffix_exception_text(self):
        return self.get_element_text(*SuffixPage.name_noneText)
    # 后缀名搜索验证信息
    def search_suffix_text(self):
        return self.get_element_text(*SuffixPage.search_suffixText)
    # 取消成功验证信息
    def cancel_suffix_text(self):
        return  self.get_element_text(*SuffixPage.cancel_suffixText)
from Page.BasePage import BasePage
from util.parseConFile import ParseConFile


class TypePage(BasePage):
    # 配置文件读取元素
    do_conf = ParseConFile()
    # 文件同步模块按钮
    loginText = do_conf.get_locators_or_account('HomePageElements', 'loginText')
    # 文件类型管理按钮
    file_typeBtn = do_conf.get_locators_or_account('TypePageElements', 'file_typeBtn')
    # 添加文件类型按钮
    add_type = do_conf.get_locators_or_account('TypePageElements', 'add_type')
    # 类型名称输入框
    type_name = do_conf.get_locators_or_account('TypePageElements', 'type_name')
    # 选择文件按钮
    choose_fileBtn = do_conf.get_locators_or_account('TypePageElements', 'choose_fileBtn')
    # 生成特征码按钮
    signatureBtn = do_conf.get_locators_or_account('TypePageElements', 'signatureBtn')
    # 保存按钮
    save_typeBtn = do_conf.get_locators_or_account('TypePageElements', 'save_typeBtn')
    # 取消按钮
    cancelBtn = do_conf.get_locators_or_account('TypePageElements', 'cancelBtn')
    # 保存成功后的验证信息
    save_typeText = do_conf.get_locators_or_account('TypePageElements', 'save_typeText')
    # 取消成功验证信息
    cancel_typeText = do_conf.get_locators_or_account('TypePageElements', 'cancel_typeText')
    # 失败/成功,确认按钮
    qdBtn = do_conf.get_locators_or_account('SharedPageElements', 'qdBtn')
    # 文件类型名称异常验证信息
    name_noneText = do_conf.get_locators_or_account('TypePageElements', 'name_noneText')
    # 只输入名称,不选择文件验证信息
    file_noneText = do_conf.get_locators_or_account('TypePageElements', 'file_noneText')
    #文件类型列表复选框按钮,全选和按照顺序选
    all_selectBtn = do_conf.get_locators_or_account('TypePageElements', 'all_selectBtn')
    select_typeBtn1 = do_conf.get_locators_or_account('TypePageElements', 'select_typeBtn1')
    select_typeBtn2 = do_conf.get_locators_or_account('TypePageElements', 'select_typeBtn2')
    select_typeBtn3 = do_conf.get_locators_or_account('TypePageElements', 'select_typeBtn3')
    #文件类型删除按钮
    delete_typeBtn = do_conf.get_locators_or_account('TypePageElements', 'delete_typeBtn')
    #搜索输入框
    search_type = do_conf.get_locators_or_account('TypePageElements', 'search_type')
    #搜索验证信息
    search_typeText = do_conf.get_locators_or_account('TypePageElements', 'search_typeText')


    # 进入文件类型管理页面
    def type_process(self):
        self.sleep(0.5)
        self.click(*TypePage.loginText)
        self.sleep(1)
        self.click(*TypePage.file_typeBtn)
        iframe = self.driver.find_element_by_tag_name('iframe')
        self.driver.switch_to_frame(iframe)
    # 添加文件类型流程
    def add_type_process(self,route,name):
        self.type_process()
        self.click(*TypePage.add_type)
        self.sleep(2)
        self.find_element(*TypePage.choose_fileBtn).send_keys(route)
        self.sleep(0.5)
        self.click(*TypePage.signatureBtn)
        self.sleep(0.5)
        self.find_element(*TypePage.type_name).send_keys(name)
        self.click(*TypePage.save_typeBtn)
        self.sleep(1)

    # 添加文件类型流程,超长名称字符
    def add_type_process_superLongName(self, route, name):
        self.type_process()
        self.sleep(1)
        self.click(*TypePage.add_type)
        self.sleep(0.5)
        self.find_element(*TypePage.choose_fileBtn).send_keys(route)
        self.sleep(1)
        self.click(*TypePage.signatureBtn)
        self.sleep(0.5)
        self.find_element(*TypePage.type_name).send_keys(name)
        self.click(*TypePage.save_typeBtn)
        self.sleep(1)


    # 添加文件类型流程,名称为空
    def add_type_process_noneName(self,route):
        self.type_process()
        self.sleep(1)
        self.click(*TypePage.add_type)
        self.sleep(1)
        self.find_element(*TypePage.choose_fileBtn).send_keys(route)
        self.sleep(1)
        self.click(*TypePage.signatureBtn)
        self.click(*TypePage.save_typeBtn)
        self.sleep(1)

    # 添加文件类型流程,名称为空格
    def add_type_process_spaceName(self,route,name):
        self.type_process()
        self.sleep(1)
        self.click(*TypePage.add_type)
        self.sleep(1)
        self.find_element(*TypePage.choose_fileBtn).send_keys(route)
        self.find_element(*TypePage.type_name).send_keys(name)
        self.sleep(1)
        self.click(*TypePage.signatureBtn)
        self.click(*TypePage.save_typeBtn)
        self.sleep(1)

    # 添加文件类型流程,直接保存
    def add_type_process_directSave(self):
        self.type_process()
        self.sleep(1)
        self.click(*TypePage.add_type)
        self.sleep(1)
        self.click(*TypePage.save_typeBtn)
        self.sleep(1)
    # 添加文件类型流程,不选择文件保存
    def add_type_process_nonefile(self,name):
        self.type_process()
        self.sleep(1)
        self.click(*TypePage.add_type)
        self.find_element(*TypePage.type_name).send_keys(name)
        self.sleep(1)
        self.click(*TypePage.save_typeBtn)
        self.sleep(1)

    # 添加文件类型流程,选择文件但不生成特征码保存
    def add_type_process_nonefileCode(self, route, name):
        self.type_process()
        self.sleep(1)
        self.click(*TypePage.add_type)
        self.sleep(1)
        self.find_element(*TypePage.choose_fileBtn).send_keys(route)
        self.find_element(*TypePage.type_name).send_keys(name)
        self.sleep(1)
        self.click(*TypePage.save_typeBtn)
        self.sleep(1)

    # 添加文件类型流程,取消
    def add_type_process_cancel(self):
        self.type_process()
        self.sleep(1)
        self.click(*TypePage.add_type)
        self.sleep(1)
        self.click(*TypePage.cancelBtn)
        self.sleep(2)

    # 搜索流程
    def search_type_process(self, searchData):
        self.type_process()
        self.sleep(1)
        self.find_element(*TypePage.search_type).send_keys(searchData)
        self.sleep(1)

        # 删除文件类型流程,单选未被使用

    def delete_type_noSelect(self):
        self.type_process()
        self.sleep(1)
        self.click(*TypePage.delete_typeBtn)
        self.sleep(1)

    # 删除文件类型流程,单选未被使用
    def delete_type_single(self):
        self.type_process()
        self.sleep(1)
        self.click(*TypePage.select_typeBtn1)
        self.sleep(1)
        self.click(*TypePage.delete_typeBtn)
        self.sleep(0.5)
        self.click(*TypePage.qdBtn)
        self.sleep(1)

    # 删除文件类型流程,单选被使用
    def delete_type_singleEmploy(self):
        self.type_process()
        self.sleep(1)
        self.click(*TypePage.select_typeBtn2)
        self.sleep(1)
        self.click(*TypePage.delete_typeBtn)
        self.sleep(0.5)
        self.click(*TypePage.qdBtn)
        self.sleep(1)

    # 删除文件类型流程,多选
    def delete_type_multipleChoice(self):
        self.type_process()
        self.sleep(1)
        self.click(*TypePage.select_typeBtn2)
        self.click(*TypePage.select_typeBtn3)
        self.sleep(1)
        self.click(*TypePage.delete_typeBtn)
        self.sleep(0.5)
        self.click(*TypePage.qdBtn)
        self.sleep(1)

    # 删除文件类型流程,全选
    def delete_type_allSelect(self):
        self.type_process()
        self.sleep(1)
        self.click(*TypePage.all_selectBtn)
        self.sleep(1)
        self.click(*TypePage.delete_typeBtn)
        self.sleep(0.5)
        self.click(*TypePage.qdBtn)
        self.sleep(1)
    # 保存成功和失败验证信息
    def save_type_text(self):
        return self.get_element_text(*TypePage.save_typeText)

    # 取消验证信息
    def cancel_type_text(self):
        return self.get_element_text(*TypePage.cancel_typeText)

    # 搜索验证信息
    def search_type_text(self):
        return self.get_element_text(*TypePage.search_typeText)

    # 异常提示验证信息
    def Tips_text(self):
        return self.get_element_text(*TypePage.name_noneText)













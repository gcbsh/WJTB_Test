from Page.BasePage import BasePage
from util.parseConFile import ParseConFile


class ContentPage(BasePage):
    # 配置文件读取元素
    do_conf = ParseConFile()
    # 文件同步模块按钮
    loginText = do_conf.get_locators_or_account('HomePageElements', 'loginText')
    # 文件内容过滤管理按钮
    contentBtn = do_conf.get_locators_or_account('ContentPageElements', 'contentBtn')
    # 内容添加按钮
    add_contentBtn = do_conf.get_locators_or_account('ContentPageElements', 'add_contentBtn')
    # 内容输入框
    contentBox = do_conf.get_locators_or_account('ContentPageElements', 'contentBox')
    # 保存内容按钮
    save_content = do_conf.get_locators_or_account('ContentPageElements', 'save_content')
    # 保存成功后的验证信息
    save_contentText = do_conf.get_locators_or_account('ContentPageElements', 'save_contentText')
    # 失败/成功,确认按钮
    qdBtn = do_conf.get_locators_or_account('SharedPageElements', 'qdBtn')
    #搜索输入框
    search_content = do_conf.get_locators_or_account('ContentPageElements', 'search_content')
    #取消按钮
    cancel_contentBtn = do_conf.get_locators_or_account('ContentPageElements', 'cancel_contentBtn')
    # 删除按钮
    deleteBtn = do_conf.get_locators_or_account('ContentPageElements', 'deleteBtn')
    #取消验证信息
    cancel_suffixText = do_conf.get_locators_or_account('ContentPageElements', 'cancel_suffixText')
    # 内容错误验证信息
    error_contentText = do_conf.get_locators_or_account('ContentPageElements', 'error_contentText')
    #搜索验证信息
    search_contentText = do_conf.get_locators_or_account('ContentPageElements', 'search_contentText')
    # 文件后缀名列表复选框按钮, 全选和按照顺序选
    all_selectBtn = do_conf.get_locators_or_account('ContentPageElements', 'all_selectBtn')
    select_contentBtn1 = do_conf.get_locators_or_account('ContentPageElements', 'select_contentBtn1')
    select_contentBtn2 = do_conf.get_locators_or_account('ContentPageElements', 'select_contentBtn2')
    select_contentBtn3 = do_conf.get_locators_or_account('ContentPageElements', 'select_contentBtn3')

    # 进入文件内容过滤页面
    def add_content(self):
        self.click(*ContentPage.loginText)
        self.sleep(1)
        self.click(*ContentPage.contentBtn)
        iframe = self.driver.find_element_by_tag_name('iframe')
        self.driver.switch_to_frame(iframe)
    # 添加文件内容过滤流程
    def add_content_process(self,content):
        self.add_content()
        self.sleep(0.5)
        self.click(*ContentPage.add_contentBtn)
        self.find_element(*ContentPage.contentBox).send_keys(content)
        self.click(*ContentPage.save_content)
        self.sleep(1)
    # 添加文件内容过滤,为空
    def add_content_none(self):
        self.add_content()
        self.sleep(0.5)
        self.click(*ContentPage.add_contentBtn)
        self.click(*ContentPage.save_content)
        self.sleep(1)
    # 添加文件内容过滤,取消
    def add_content_cancel(self):
        self.add_content()
        self.sleep(0.5)
        self.click(*ContentPage.add_contentBtn)
        self.click(*ContentPage.cancel_contentBtn)
        self.sleep(1)
    # 搜索文件内容过滤流程
    def search_content_process(self,searchData):
        self.add_content()
        self.sleep(0.5)
        self.find_element(*ContentPage.search_content).send_keys(searchData)
        self.sleep(1)
    # 删除文件内容过滤,不选择列表
    def delete_content_noSeletect(self):
        self.add_content()
        self.sleep(0.5)
        self.click(*ContentPage.deleteBtn)
        self.sleep(1)
    # 删除文件内容过滤,单选未被任务使用
    def delete_content_single(self):
        self.add_content()
        self.sleep(0.5)
        self.click(*ContentPage.select_contentBtn2)
        self.click(*ContentPage.deleteBtn)
        self.sleep(0.5)
        self.click(*ContentPage.qdBtn)
        self.sleep(1)
    # 删除文件内容过滤,单选被任务使用
    def delete_content_singleEmploy(self):
        self.add_content()
        self.sleep(0.5)
        self.click(*ContentPage.select_contentBtn1)
        self.click(*ContentPage.deleteBtn)
        self.sleep(0.5)
        self.click(*ContentPage.qdBtn)
        self.sleep(1)
    # 删除文件内容过滤,多选
    def delete_content_multipleChoice(self):
        self.add_content()
        self.sleep(0.5)
        self.click(*ContentPage.select_contentBtn2)
        self.click(*ContentPage.select_contentBtn3)
        self.click(*ContentPage.deleteBtn)
        self.sleep(0.5)
        self.click(*ContentPage.qdBtn)
        self.sleep(1)
    # 删除文件内容过滤,全选
    def delete_content_allSelect(self):
        self.add_content()
        self.sleep(0.5)
        self.click(*ContentPage.all_selectBtn)
        self.click(*ContentPage.deleteBtn)
        self.sleep(0.5)
        self.click(*ContentPage.qdBtn)
        self.sleep(1)


    # 保存成功验证信息
    def save_content_text(self):
        return self.get_element_text(*ContentPage.save_contentText)
    # 内容错误验证信息
    def content_error_text(self):
        return self.get_element_text(*ContentPage.error_contentText)
    # 取消验证信息
    def content_cancel_text(self):
        return self.get_element_text(*ContentPage.cancel_suffixText)
    # 搜索验证信息
    def content_search_text(self):
        return self.get_element_text(*ContentPage.search_contentText)





































































from Page.BasePage import BasePage
from util.parseConFile import ParseConFile
from selenium.webdriver.support.select import Select


class SharedPage(BasePage):
    # 配置文件读取元素
    do_conf = ParseConFile()
    # 文件同步模块按钮
    loginText = do_conf.get_locators_or_account('HomePageElements', 'loginText')
    # 共享目录按钮
    sharedBtn = do_conf.get_locators_or_account('SharedPageElements', 'sharedBtn')
    # 添加按钮
    addBtn = do_conf.get_locators_or_account('SharedPageElements', 'addBtn')
    # smb ip输入框
    smbip = do_conf.get_locators_or_account('SharedPageElements', 'smbip')
    # smb目录输入框
    smbmulu = do_conf.get_locators_or_account('SharedPageElements', 'smbmulu')
    # smb用户输入框
    smbuser = do_conf.get_locators_or_account('SharedPageElements', 'smbuser')
    # smb密码输入框
    smbpw  = do_conf.get_locators_or_account('SharedPageElements', 'smbpw')
    #选择共享类型按钮
    shared_typeBtn = do_conf.get_locators_or_account('SharedPageElements', 'shared_typeBtn')
    #nfs类型
    nfsType = do_conf.get_locators_or_account('SharedPageElements', 'nfsType')
    #;nfs ip 输入框
    nfsip = do_conf.get_locators_or_account('SharedPageElements', 'nfsip')
    #nfs共享目录输入框
    nfsmulu = do_conf.get_locators_or_account('SharedPageElements', 'nfsmulu')
    # 测试连接按钮
    testBtn = do_conf.get_locators_or_account('SharedPageElements', 'testBtn')
    # 保存按钮
    saveBtn = do_conf.get_locators_or_account('SharedPageElements', 'saveBtn')
    # 保存成功验证信息
    saveText = do_conf.get_locators_or_account('SharedPageElements', 'saveText')
    # 外端共享目录按钮
    waiBtn = do_conf.get_locators_or_account('SharedPageElements', 'waiBtn')
    # 测试连接成功验证信息
    test_Text = do_conf.get_locators_or_account('SharedPageElements', 'test_Text')
    # （关闭测试连接成功/失败信息）确定按钮
    qdBtn = do_conf.get_locators_or_account('SharedPageElements', 'qdBtn')
    # （关闭保存成功/失败信息）确定按钮

    # 选择共享类型
    def select_shareType(self):
        return Select(self.find_element(*SharedPage.shared_typeBtn))
    # 创建内端共享目录流程
    def shared(self):
        self.sleep(1)
        self.click(*SharedPage.loginText)
        self.sleep(1)
        self.click(*SharedPage.sharedBtn)
        iframe = self.driver.find_element_by_tag_name('iframe')
        self.driver.switch_to_frame(iframe)
        self.sleep(0.5)
        self.click(*SharedPage.addBtn)
        self.sleep(0.5)
        self.find_element(*SharedPage.smbip).send_keys('192.168.3.42')
        self.sleep(0.5)
        self.find_element(*SharedPage.smbmulu).send_keys('smbsend')
        self.find_element(*SharedPage.smbuser).send_keys('smbuser')
        self.find_element(*SharedPage.smbpw).send_keys('000')
        self.sleep(1)
        self.click(*SharedPage.testBtn)
        self.sleep(3)
        result = self.get_element_text(*SharedPage.test_Text)
        self.click(*SharedPage.qdBtn)
        self.sleep(2)
        self.click(*SharedPage.saveBtn)
        self.sleep(3)
        self.click(*SharedPage.qdBtn)
        return result

        # 创建内端共享目录流程
    def shared_nfs(self):
        self.sleep(1)
        self.click(*SharedPage.loginText)
        self.sleep(1)
        self.click(*SharedPage.sharedBtn)
        iframe = self.driver.find_element_by_tag_name('iframe')
        self.driver.switch_to_frame(iframe)
        self.sleep(0.5)
        self.click(*SharedPage.addBtn)
        self.sleep(0.5)
        self.select_shareType().select_by_index(*SharedPage.nfsType)
        self.sleep(0.5)
        self.find_element(*SharedPage.nfsip).send_keys('192.168.3.42')
        self.sleep(0.5)
        self.find_element(*SharedPage.nfsmulu).send_keys('data/nfssend')
        self.sleep(1)
        self.click(*SharedPage.testBtn)
        self.sleep(3)
        result = self.get_element_text(*SharedPage.test_Text)
        self.click(*SharedPage.qdBtn)
        self.sleep(2)
        self.click(*SharedPage.saveBtn)
        self.sleep(3)
        self.click(*SharedPage.qdBtn)
        return result
    # 创建外端共享目录流程
    def shared_wai(self):
        # self.click(*SharedPage.loginText)
        self.sleep(1)
        # self.click(*SharedPage.sharedBtn)
        # iframe = self.driver.find_element_by_tag_name('iframe')
        # self.driver.switch_to_frame(iframe)
        self.click(*SharedPage.waiBtn)
        self.sleep(0.5)
        self.click(*SharedPage.addBtn)
        self.sleep(0.5)
        self.find_element(*SharedPage.smbip).send_keys('192.168.3.15')
        self.sleep(0.5)
        self.find_element(*SharedPage.smbmulu).send_keys('smbreceive')
        self.find_element(*SharedPage.smbuser).send_keys('smbuser')
        self.find_element(*SharedPage.smbpw).send_keys('000')
        self.sleep(1)
        self.click(*SharedPage.testBtn)
        self.sleep(3)
        result = self.get_element_text(*SharedPage.test_Text)
        self.click(*SharedPage.qdBtn)
        self.sleep(2)
        self.click(*SharedPage.saveBtn)
        self.sleep(1)
        return result
    def shared_nfs_wai(self):
        # self.click(*SharedPage.loginText)
        self.sleep(1)
        # self.click(*SharedPage.sharedBtn)
        # iframe = self.driver.find_element_by_tag_name('iframe')
        # self.driver.switch_to_frame(iframe)
        self.click(*SharedPage.waiBtn)
        self.sleep(1)
        self.click(*SharedPage.addBtn)
        # self.sleep(0.5)
        # self.click(*SharedPage.shared_typeBtn)
        self.sleep(0.5)
        self.select_shareType().select_by_index(*SharedPage.nfsType)
        self.sleep(0.5)
        self.find_element(*SharedPage.nfsip).send_keys('192.168.3.42')
        self.sleep(0.5)
        self.find_element(*SharedPage.nfsmulu).send_keys('data/nfssend')
        self.sleep(1)
        self.click(*SharedPage.testBtn)
        self.sleep(3)
        result = self.get_element_text(*SharedPage.test_Text)
        self.click(*SharedPage.qdBtn)
        self.sleep(2)
        self.click(*SharedPage.saveBtn)
        self.sleep(3)
        self.click(*SharedPage.qdBtn)
        return result
    def test_text(self):
        return self.get_element_text(*SharedPage.test_Text)

    def save_text(self):
        return self.get_element_text(*SharedPage.saveText)


if __name__ == "__main__":
    pass






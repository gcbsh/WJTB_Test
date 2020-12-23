from Page.BasePage import BasePage
from util.parseConFile import ParseConFile


class SynchronizePage(BasePage):
    # 配置文件读取元素
    do_conf = ParseConFile()
    # 文件同步模块按钮
    loginText = do_conf.get_locators_or_account('HomePageElements', 'loginText')
    # 同步任务管理模块按钮
    synchronizeBtn = do_conf.get_locators_or_account('SynchronizePageElements', 'synchronizeBtn')
    # 添加任务按钮
    add_task = do_conf.get_locators_or_account('SynchronizePageElements', 'add_task')
    # 任务名称输入框
    task_name = do_conf.get_locators_or_account('SynchronizePageElements', 'task_name')
    # 内端目录复选框
    smb3_42nei = do_conf.get_locators_or_account('SynchronizePageElements', 'smb3_42nei')
    # 外端目录复选框
    smb3_15wai = do_conf.get_locators_or_account('SynchronizePageElements', 'smb3_15wai')
    # 保存任务按钮
    save_taskBtn = do_conf.get_locators_or_account('SynchronizePageElements', 'save_taskBtn')
    # 保存成功/失败后的确定按钮
    qd_task = do_conf.get_locators_or_account('SynchronizePageElements', 'qd_task')
    # 保存成功的验证信息
    save_taskText = do_conf.get_locators_or_account('SynchronizePageElements', 'save_taskText')
    # 任务复选框
    taskBox = do_conf.get_locators_or_account('SynchronizePageElements', 'taskBox')
    # 启动任务按钮
    startBtn = do_conf.get_locators_or_account('SynchronizePageElements', 'startBtn')
    # 停止任务按钮
    stopBtn = do_conf.get_locators_or_account('SynchronizePageElements', 'stopBtn')

    # 创建同步任务并启用，停止流程
    def create_task(self):
        self.sleep(0.5)
        self.click(*SynchronizePage.loginText)
        self.sleep(1)
        self.click(*SynchronizePage.synchronizeBtn)
        iframe = self.driver.find_element_by_tag_name('iframe')
        self.driver.switch_to_frame(iframe)
        self.sleep(0.5)
        self.click(*SynchronizePage.add_task)
        self.find_element(*SynchronizePage.task_name).send_keys('3.42-3.15nei-wai')
        self.click(*SynchronizePage.smb3_42nei)
        self.click(*SynchronizePage.smb3_15wai)
        self.click(*SynchronizePage.save_taskBtn)
        result = self.get_element_text(*SynchronizePage.save_taskText)
        self.sleep(1)
        self.click(*SynchronizePage.qd_task)
        self.sleep(1)
        self.click(*SynchronizePage.taskBox)
        self.sleep(0.5)
        self.click(*SynchronizePage.startBtn)
        self.sleep(2)
        result2 = self.get_element_text(*SynchronizePage.save_taskText)
        self.sleep(1)
        self.click(*SynchronizePage.qd_task)
        self.sleep(1)
        self.click(*SynchronizePage.stopBtn)
        self.sleep(3)
        return result, result2

    def save_task_text(self):
        return self.get_element_text(*SynchronizePage.save_taskText)







from Page.BasePage import BasePage
from util.parseConFile import ParseConFile


class LoginPage(BasePage):
    # 配置文件读取元素
    do_conf = ParseConFile()
    # 高级按钮
    detailsBtn = do_conf.get_locators_or_account('httpsVerificationElements', 'detailsBtn')
    # 前往url
    proceedBtn = do_conf.get_locators_or_account('httpsVerificationElements', 'proceedBtn')
    # 用户名输入框
    username = do_conf.get_locators_or_account('LoginPageElements', 'username')
    # 密码输入框
    password = do_conf.get_locators_or_account('LoginPageElements', 'password')
    # 登录按钮
    loginBtn = do_conf.get_locators_or_account('LoginPageElements', 'loginBtn')
    # 登录成功后的显示元素
    loginText = do_conf.get_locators_or_account('HomePageElements', 'loginText')

    def login(self, username, password):
        """登录流程"""
        self.open_url()
        self.click(*LoginPage.detailsBtn)
        self.click(*LoginPage.proceedBtn)
        self.sleep(2)
        self.find_element(*LoginPage.username).send_keys(username)
        self.find_element(*LoginPage.password).send_keys(password)
        self.click(*LoginPage.loginBtn)
        self.sleep(2)


    def open_url(self):
        return self.load_url('https://192.168.0.28')

    def login_text(self):
        return self.get_element_text(*LoginPage.loginText)


if __name__ == "__main__":
    pass

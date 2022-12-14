from selenium import webdriver
class Login:
    textbox_username_id = "Email"
    textbox_passwords_id = "Password"
    butoon_login_xpath ="//button[normalize-space()='Log in']"
    link_logout_linktext ="Logout"

    def __init__(self, driver):
        self.driver = driver
    def setUserName(self,username):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_username_id).send_key(username)


    def setpassword(self, password):
        self.driver.find_element_by_id(self.textbox_passwords_id).clear()
        self.driver.find_element_by_id(self.textbox_passwords_id).send_key(password)

    def clicklogion(self):
        self.driver.find_element_by_xpath(self.butoon_login_xpath).click()
    def clicklogout(self):
        self.driver.find_element_by_link(self.link_logout_linktext)
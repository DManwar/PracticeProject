import pytest
from selenium import webdriver
from PageObjects.Loginpage import Login
from Utilities.readProperties import Readconfig
from Utilities.customLogger import LogGen

class Test_001_Login:
    baseURL = Readconfig.getApplicationURL()
    username = Readconfig.getUseremail()
    password = Readconfig.getPassword()

    logger=LogGen.loggen()

    def test_homePageTitle(self,setup):
        self.logger.info("************ Test_001_Login ***************************")
        self.logger.info("****************Started Home Page Title test ****************")
        self.driver= setup
        self.logger.info("************ opening url ***************************")
        self.driver.get(self.baseURL)
        act_title =self.driver.tille
        self.driver.close()
        if act_title == "Your store. Login":
            assert True
            self.logger.info("************Home page title test is passed ******************")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshot\\"+"test_homePageTitle.png")
            self.driver.close()
            self.logger.error("********************Home page title test is failed ******************")

            assert False


    def test_login(self,setup):

        self.logger.info("******************** Vrifying login test ******************")

        self.driver= setup
        self.driver.get(self.baseURL)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title=self.driver.title
        self.driver.close()
        if act_title=="Dashboard / nopCommerce administration":
            assert True
            self.logger.info("********************login test is passed ******************")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshot\\" + "test_login.png")
            self.driver.close()
            self.logger.error("********************login test is failed ******************")
            assert False

import pytest
from selenium import webdriver
from PageObjects.Loginpage import Login
from Utilities.readProperties import Readconfig
from Utilities.customLogger import LogGen
from Utilities import XLUtils


class Test_00_DDT_Login:
    baseURL = Readconfig.getApplicationURL()
    path =""
    logger=LogGen.loggen()

    def test_login(self,setup):
        self.logger.info("******************** Test_002_DDT_Login ******************")
        self.logger.info("******************** Vrifying login DDT test ******************")
        self.driver= setup
        self.driver.get(self.baseURL)

        XLUtils.getRowCount(self.path,'sheet1    * ')

*

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

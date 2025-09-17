import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pageObjects.LoginPage import LoginPage
from utilities.readproperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:
    #AS the methods define in the class readconfig is static so no need for object. it can be directly called
    baseURL=ReadConfig.getApplicationURL()
    username=ReadConfig.getUseremail()
    password=ReadConfig.getPassword()
    logger=LogGen.loggen()

    @pytest.mark.regression


    def test_homePageTitle(self,setup):
        self.logger.info("Test_001_login")
        self.logger.info("***********verify home page title***********")
        self.driver= setup
        self.driver.get(self.baseURL)
        time.sleep(5)
        act_title=self.driver.title


        if act_title=="nopCommerce demo store. Login":
            assert True
            self.driver.close()
            self.logger.info("*****home page title test is passes*****")
        else:
            #for ss folder when you copy the path its showing likwthis C:\Users\bibiisha\PycharmProjects\nopcommerceApp\Screenshots you have to write it like below
            self.driver.save_screenshot("C:\\Users\\bibiisha\\PycharmProjects\\nopcommerceApp\\Screenshots\\test_homePageTitle.png")
            self.driver.close()
            self.logger.error("*****home page title is failed*****")
            assert False

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_login(self,setup):
        self.logger.info("*****verify login test*****")
        self.driver= setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        act_title=self.driver.title

        if act_title=="Dashboard / nopCommerce administration":
            assert True
            self.logger.info("*****login test is passes*****")
            self.driver.close()

        else:
            self.driver.save_screenshot("C:\\Users\\bibiisha\\PycharmProjects\\nopcommerceApp\\Screenshots\\test_login.png")
            self.driver.close()
            self.logger.error("*****login test is failed*****")
            assert False







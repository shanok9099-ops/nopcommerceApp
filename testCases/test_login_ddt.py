import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pageObjects.LoginPage import LoginPage
from utilities.readproperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import xlutility

class Test_002_DDT_Login:
    #AS the methods define in the class readconfig is static so no need for object. it can be directly called
    baseURL=ReadConfig.getApplicationURL()
    path=".//TestData/LoginData.xlsx"

    logger=LogGen.loggen()

    @pytest.mark.regression
    def test_login_ddt(self,setup):
        self.logger.info("*****Test_002_DDT_Login*****")
        self.driver= setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.rows=xlutility.getRowCount(self.path,'Sheet1')
        print("Number of rows: ", self.rows)

        lst_status=[]

        for r in range(2,self.rows+1):
            self.user=xlutility.readData(self.path,'Sheet1',r,1)
            self.password=xlutility.readData(self.path,'Sheet1',r,2)
            self.exp=xlutility.readData(self.path,'Sheet1',r,3)
            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)
            act_title=self.driver.title
            exp_title="Dashboard / nopCommerce administration"

            if act_title==exp_title:
                if self.exp=="Pass":
                    self.logger.info("**PASS")
                    self.lp.clickLogout()
                    lst_status.append('PASS')
                elif self.exp=="Fail":
                    self.logger.info("**FAIL")
                    self.lp.clickLogout()
                    lst_status.append('FAIL')
            elif act_title!=exp_title:
                if self.exp=="Pass":
                    self.logger.info("**FAIL")
                    lst_status.append('FAIL')
                elif self.exp=="Fail":
                    self.logger.info("**PASS")
                    lst_status.append('PASS')
        if "Fail" not in lst_status:
            self.logger.info("****** login DDT Test passed")
            self.driver.close()
            assert True

        else:
            self.logger.info("****** login DDT Test failed")
            self.driver.close()
            assert False


        self.logger.info("*****End of Login DDT Test")









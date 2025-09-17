import pytest
import time
from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPagePavan import AddCustomer
from utilities.readproperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random



class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_addCustomer(self, setup):
     self.logger.info("Test_003_AddCustomer")
     self.driver=setup
     self.driver.get(self.baseURL)
     self.driver.maximize_window()
     self.lp=LoginPage(self.driver)
     self.lp.setUserName(self.username)
     self.lp.setPassword(self.password)
     self.lp.clickLogin()
     self.logger.info("***Login Succesfull*****")
     self.logger.info("***start add customer****")

     self.addcust=AddCustomer(self.driver)
     self.addcust.clickOnCustomersMenu()
     self.addcust.clickOnCustomersMenuItem()

     self.addcust.clickOnAddnew()

     self.logger.info("** provide cust info****")
     self.email= random_generator() + '@gmail.com'
     self.addcust.setEmail(self.email)
     self.addcust.setPassword("test123")
     self.addcust.setCustomerRole("Guests")
     self.addcust.setManagerOfVendor("Vendor 2")
     self.addcust.setGender("Male")
     self.addcust.setFirstName("Shahnaz")
     self.addcust.setLastName("QA")
     self.addcust.setCompanyName("QA testing")
     self.addcust.setAdminContent("this is for testing")
     self.addcust.clickOnSave()


     self.logger.info("***saving customer info****")
     self.logger.info("***add customer validation info****")
     self.msg= self.driver.find_element(By.TAG_NAME,"body").text

     print(self.msg)
     if 'customer has been added successfully.' in self.msg:
         assert True==True
         self.logger.info("***add customer test pass****")
     else:
        # self.driver.save_screenshot("C:\\Users\\bibiisha\\PycharmProjects\\nopcommerceApp\\Screenshots\\addcustomer.png")
         self.logger.info("***add customer test fail****")
         assert True==False

     self.driver.close()


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
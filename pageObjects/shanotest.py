import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AddCustomer:
    lnkCustomers_menu_xpath="//a[@href='#']//p[contains(text(),'Customers')]"
    lnkCustomers_menuitem_xpath="//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btnAddnew_xpath="//a[normalize-space()='Add new']"
    txtEmail_xpath="//input[@id='Email']"
    txtPassword_xpath="//input[@id='Password']"
    txtcustomerRoles_xpath="//*[@id='customer-info']/div[2]/div[9]/div[2]/div/div[1]/div/span/span[1]/span/ul/li/input"
    lstitemAdministration_xpath="//li[@id='select2-SelectedCustomerRoleIds-result-2eud-1']"
    lstitemFormd_xpath="//li[@id='select2-SelectedCustomerRoleIds-result-lyj8-2']"
    lstitemRegistered_xpath="//li[@id='select2-SelectedCustomerRoleIds-result-j3by-3']"
    lstitemGuests_xpath="//li[@id='select2-SelectedCustomerRoleIds-result-j6xk-4']"
    lstitemVendors_xpath="//li[@id='select2-SelectedCustomerRoleIds-result-t14g-5']"
    lstitemTrung_xpath="//li[@id='select2-SelectedCustomerRoleIds-result-9utc-6']"
    drpmgrOfVendor_xpath="//select[@id='VendorId']"
    rdMaleGenders_id="Gender_Male"
    rdFemaleGenders_id="Gender_Female"
    txtFirstName_xpath="//input[@id='FirstName']"
    txtLastName_xpath="//input[@id='LastName']"
    txtCompanyName_xpath="//input[@id='Company']"
    txtAdminContent_xpath="//textarea[@id='AdminComment']"
    btnSave_xpath="//button[@name='save']"

    def __init__(self,driver):
        self.driver = driver
    def clickOnCustomersMenu(self):
        self.driver.find_element(By.XPATH,self.lnkCustomers_menu_xpath).click()
    def clickOnCustomersMenuItem(self):
        self.driver.find_element(By.XPATH,self.lnkCustomers_menuitem_xpath).click()
    def clickOnAddnew(self):
        #self.driver.find_element(By.XPATH,self.btnAddnew_xpath).click()
        self.driver.find_element(By.XPATH, self.btnAddnew_xpath).click()
        # expand "Customer info" section
        self.driver.find_element(By.XPATH, "//div[@id='customer-info']//div[contains(@class,'card-title')]").click()

    def setEmail(self, email):
        # expand "Customer info" panel if collapsed
        try:
            self.driver.find_element(
                By.XPATH, "//div[@id='customer-info']//div[contains(@class,'card-title')]//button"
            ).click()
        except Exception:
            pass  # already open

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.txtEmail_xpath))
        ).send_keys(email)

            # WebDriverWait(self.driver, 10).until(
            #     EC.visibility_of_element_located((By.XPATH, self.txtEmail_xpath))
            # ).send_keys(email)


    #def setEmail(self,email):
        #self.driver.find_element(By.XPATH,self.txtEmail_xpath).send_keys(email)
    def setPassword(self,password):
        #self.driver.find_element(By.XPATH,self.txtPassword_xpath).send_keys(password)
        # ensure the section is open (no-op if already open)
        try:
            self.driver.find_element(
                By.XPATH, "//div[@id='customer-info']//div[contains(@class,'card-title')]"
            ).click()
        except Exception:
            pass

        el = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.txtPassword_xpath))
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", el)
        try:
            el.clear()
        except Exception:
            pass
        el.send_keys(password)
    def setCustomerRole(self,role):
         self.driver.find_element(By.XPATH,self.txtcustomerRoles_xpath).click()
         time.sleep(3)
         if role=='Registered':
             self.listitem=self.driver.find_element(By.XPATH,self.lstitemRegistered_xpath)
         elif role=='Administrators':
             self.listitem=self.driver.find_element(By.XPATH,self.lstitemAdministration_xpath)
         elif role=='Guests':
                time.sleep(3)
             #self.driver.find_element(By.XPATH,"//*[@id='SelectCustomerRoleIds_taglist']/li/span[2]").click()
             #self.listitem=self.driver.find_element(By.XPATH,self.lstitemGuests_xpath)


         elif role=='Vendor':
            self.listitem=self.driver.find_element(By.XPATH,self.lstitemVendors_xpath)
         elif role=='Trung':
             self.listitem=self.driver.find_element(By.XPATH,self.lstitemTrung_xpath)
         elif role=='Forum Moderators':
            self.listitem=self.driver.find_element(By.XPATH,self.lstitemFormd_xpath)
         else:
             self.listitem=self.driver.find_element(By.XPATH,self.lstitemGuests_xpath)
         time.sleep(3)
         self.driver.execute_script("arguments[0].click();", self.listitem)


    def setManagerOfVendor(self,value):
        drp=Select(self.driver.find_element(By.XPATH,self.drpmgrOfVendor_xpath))
        drp.select_by_visible_text(value)

    def setGender(self,gender):
        if gender == 'Male':
            self.driver.find_element(By.ID,self.rdMaleGenders_id).click()
        elif gender == 'Female':
            self.driver.find_element(By.ID,self.rdFemaleGenders_id).click()
        else:
            self.driver.find_element(By.ID, self.rdMaleGenders_id).click()
    def setFirstName(self,fname):
        self.driver.find_element(By.XPATH,self.txtFirstName_xpath).send_keys(fname)
    def setLastName(self,lname):
        self.driver.find_element(By.XPATH,self.txtLastName_xpath).send_keys(lname)
    def setCompanyName(self,comname):
        self.driver.find_element(By.XPATH,self.txtCompanyName_xpath).send_keys(comname)
    def setAdminContent(self,content):
        self.driver.find_element(By.XPATH,self.txtAdminContent_xpath).send_keys(content)
    def clickOnSave(self):
        self.driver.find_element(By.XPATH,self.btnSave_xpath).click()


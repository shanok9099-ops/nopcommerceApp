import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class AddCustomer:
    lnkCustomers_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    lnkCustomers_menuitem_xpath = "//a[@href='/Admin/Customer/List']"
    btnAddnew_xpath = "//a[normalize-space()='Add new']"
    txtEmail_xpath = "//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"
    # this points to the select2 roles box
    txtcustomerRoles_xpath = "//*[@id='customer-info']//span[@class='select2-selection select2-selection--multiple']"
    drpmgrOfVendor_xpath = "//select[@id='VendorId']"
    rdMaleGenders_id = "Gender_Male"
    rdFemaleGenders_id = "Gender_Female"
    txtFirstName_xpath = "//input[@id='FirstName']"
    txtLastName_xpath = "//input[@id='LastName']"
    txtCompanyName_xpath = "//input[@id='Company']"
    txtAdminContent_xpath = "//textarea[@id='AdminComment']"
    btnSave_xpath = "//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomersMenu(self):
        self.driver.find_element(By.XPATH, self.lnkCustomers_menu_xpath).click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.lnkCustomers_menuitem_xpath))
        )

    def clickOnCustomersMenuItem(self):
        self.driver.find_element(By.XPATH, self.lnkCustomers_menuitem_xpath).click()

    def clickOnAddnew(self):
        self.driver.find_element(By.XPATH, self.btnAddnew_xpath).click()
        # expand Customer info section if collapsed
        try:
            self.driver.find_element(
                By.XPATH, "//div[@id='customer-info']//div[contains(@class,'card-title')]"
            ).click()
        except:
            pass

    def setEmail(self, email):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.txtEmail_xpath))
        ).send_keys(email)

    def setPassword(self, password):
        el = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.txtPassword_xpath))
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", el)
        try:
            el.clear()
        except Exception:
            pass
        el.send_keys(password)

    def setCustomerRole(self, role):
        wait = WebDriverWait(self.driver, 10)

        # remove any preselected role (e.g., "Registered")
        try:
            while True:
                delete_btn = self.driver.find_element(
                    By.XPATH, "//ul[@id='SelectedCustomerRoleIds_taglist']//span[@title='delete']"
                )
                delete_btn.click()
        except:
            pass

        # open dropdown
        self.driver.find_element(By.XPATH, self.txtcustomerRoles_xpath).click()

        # select the role by visible text
        option_xpath = f"//li[contains(@id,'select2-SelectedCustomerRoleIds') and normalize-space()='{role}']"
        wait.until(EC.visibility_of_element_located((By.XPATH, option_xpath))).click()

    def setManagerOfVendor(self, value):
        drp = Select(self.driver.find_element(By.XPATH, self.drpmgrOfVendor_xpath))
        drp.select_by_visible_text(value)

    def setGender(self, gender):
        if gender == 'Male':
            self.driver.find_element(By.ID, self.rdMaleGenders_id).click()
        elif gender == 'Female':
            self.driver.find_element(By.ID, self.rdFemaleGenders_id).click()
        else:
            self.driver.find_element(By.ID, self.rdMaleGenders_id).click()

    def setFirstName(self, fname):
        self.driver.find_element(By.XPATH, self.txtFirstName_xpath).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element(By.XPATH, self.txtLastName_xpath).send_keys(lname)

    def setCompanyName(self, comname):
        self.driver.find_element(By.XPATH, self.txtCompanyName_xpath).send_keys(comname)

    def setAdminContent(self, content):
        self.driver.find_element(By.XPATH, self.txtAdminContent_xpath).send_keys(content)

    def clickOnSave(self):
        self.driver.find_element(By.XPATH, self.btnSave_xpath).click()


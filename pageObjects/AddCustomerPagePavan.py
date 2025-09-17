# file: pageObjects/AddCustomerPagePavan.py

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException


class AddCustomer:
    # Navigation/menu
    lnkCustomers_menu_xpath = "//a[.//p[normalize-space()='Customers'] and contains(@class,'nav-link')]"
    lnkCustomers_menuitem_xpath = "//a[@href='/Admin/Customer/List']//p[normalize-space()='Customers']"

    # Buttons & panels
    btnAddnew_xpath = "//a[normalize-space()='Add new']"
    panel_customer_info_xpath = "//div[@id='customer-info']"
    panel_customer_info_toggle_btn_xpath = "//div[@id='customer-info']//button[@data-card-widget='collapse']"
    panel_customer_info_body_xpath = "//div[@id='customer-info']//div[contains(@class,'card-body')]"

    # Fields
    txtEmail_xpath = "//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"

    # Select2 (Customer roles)
   # roles_combobox_xpath = "//span[contains(@class,'select2-selection--multiple')]"
    roles_combobox_xpath = "//div[@id='SelectedCustomerRoleIds']//span[contains(@class,'select2-selection--multiple')]"
    role_option_by_text_xpath = "//li[contains(@class,'select2-results__option') and normalize-space()='{text}']"
    select2_search_input_css = "input.select2-search__field"
    select2_results_css = ".select2-container--open .select2-results__options"

    # Other fields
    drpmgrOfVendor_xpath = "//select[@id='VendorId']"
    rdMaleGenders_id = "Gender_Male"
    rdFemaleGenders_id = "Gender_Female"
    txtFirstName_xpath = "//input[@id='FirstName']"
    txtLastName_xpath = "//input[@id='LastName']"
    txtCompanyName_xpath = "//input[@id='Company']"
    txtAdminContent_xpath = "//textarea[@id='AdminComment']"
    btnSave_xpath = "//button[@name='save']"

    # Common overlays (AdminLTE / nopCommerce)
    overlay_css = ".overlay, .loading, .pace, .pace-active"

    def __init__(self, driver, timeout: int = 15):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    # ---------------- helpers ----------------
    def wait_invisibility_of_overlays(self, timeout=20):
        """Wait until common loading overlays disappear."""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.invisibility_of_element_located((By.CSS_SELECTOR, self.overlay_css))
            )
        except Exception:
            pass

    def wait_and_click(self, by, locator):
        """Robust click with scroll + JS fallback if intercepted."""
        el = self.wait.until(EC.element_to_be_clickable((by, locator)))
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", el)
        try:
            el.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", el)

    def ensure_customer_info_expanded(self):
        """Ensure 'Customer info' card is expanded, regardless of theme/variant."""
        try:
            body = self.driver.find_element(By.XPATH, self.panel_customer_info_body_xpath)
            if not body.is_displayed():
                self.wait_and_click(By.XPATH, self.panel_customer_info_toggle_btn_xpath)
                self.wait.until(EC.visibility_of_element_located((By.XPATH, self.panel_customer_info_body_xpath)))
        except Exception:
            try:
                header_btn = self.driver.find_element(
                    By.XPATH, "//div[@id='customer-info']//div[contains(@class,'card-header')]//button"
                )
                header_btn.click()
                self.wait.until(EC.visibility_of_element_located((By.XPATH, self.panel_customer_info_body_xpath)))
            except Exception:
                pass

    def close_select2_dropdown(self):
        """Closes any open Select2 dropdown using ESC and waits until gone."""
        try:
            if self.driver.find_elements(By.CSS_SELECTOR, ".select2-container--open"):
                self.driver.switch_to.active_element.send_keys(Keys.ESCAPE)
                WebDriverWait(self.driver, 5).until(
                    EC.invisibility_of_element_located(
                        (By.CSS_SELECTOR, ".select2-container--open .select2-results")
                    )
                )
        except Exception:
            pass

    # ---------------- flows ----------------
    def clickOnCustomersMenu(self):
        self.wait_and_click(By.XPATH, self.lnkCustomers_menu_xpath)

    def clickOnCustomersMenuItem(self):
        self.wait_and_click(By.XPATH, self.lnkCustomers_menuitem_xpath)
        self.wait_invisibility_of_overlays()

    def clickOnAddnew(self):
        self.wait_and_click(By.XPATH, self.btnAddnew_xpath)
        self.wait.until(EC.url_contains("/Admin/Customer/Create"))
        self.wait_invisibility_of_overlays()
        self.ensure_customer_info_expanded()
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.txtEmail_xpath)))

    def setEmail(self, email):
        self.ensure_customer_info_expanded()
        el = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.txtEmail_xpath)))
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", el)
        try:
            el.clear()
        except Exception:
            pass
        el.send_keys(email)

    def setPassword(self, password):
        self.ensure_customer_info_expanded()
        el = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.txtPassword_xpath)))
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", el)
        try:
            el.clear()
        except Exception:
            pass
        el.send_keys(password)

    def setCustomerRole(self, role_text: str):
        def setCustomerRole(self, role_text: str):
            # Click the Customer roles select2 box
            self.wait_and_click(By.XPATH, self.roles_combobox_xpath)

            # Remove any pre-selected roles
            try:
                for pill_remove in self.driver.find_elements(
                        By.XPATH,
                        "//*[@id='SelectedCustomerRoleIds_taglist']//span[contains(@class,'select2-selection__choice__remove')]"
                ):
                    pill_remove.click()
            except Exception:
                pass

            # Type the role into the select2 search input
            search = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input.select2-search__field")))
            search.send_keys(role_text)

            # Press Enter to select the match
            search.send_keys(Keys.ENTER)

            # Close dropdown to avoid overlay issues
            self.close_select2_dropdown()
    def setManagerOfVendor(self, value):
        el = self.wait.until(EC.presence_of_element_located((By.XPATH, self.drpmgrOfVendor_xpath)))
        Select(el).select_by_visible_text(value)

    def setGender(self, gender):
        # Make sure Select2 isn't still open
        self.close_select2_dropdown()

        if str(gender).strip().lower().startswith("f"):
            self.wait_and_click(By.ID, self.rdFemaleGenders_id)
        else:
            self.wait_and_click(By.ID, self.rdMaleGenders_id)

    def setFirstName(self, fname):
        self.wait_and_click(By.XPATH, self.txtFirstName_xpath)
        self.driver.find_element(By.XPATH, self.txtFirstName_xpath).send_keys(fname)

    def setLastName(self, lname):
        self.wait_and_click(By.XPATH, self.txtLastName_xpath)
        self.driver.find_element(By.XPATH, self.txtLastName_xpath).send_keys(lname)

    def setCompanyName(self, comname):
        self.wait_and_click(By.XPATH, self.txtCompanyName_xpath)
        self.driver.find_element(By.XPATH, self.txtCompanyName_xpath).send_keys(comname)

    def setAdminContent(self, content):
        self.wait_and_click(By.XPATH, self.txtAdminContent_xpath)
        self.driver.find_element(By.XPATH, self.txtAdminContent_xpath).send_keys(content)

    def clickOnSave(self):
        self.wait_and_click(By.XPATH, self.btnSave_xpath)
        self.wait_invisibility_of_overlays()

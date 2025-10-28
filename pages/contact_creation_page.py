from pages.base_class import BaseClass

class CreateContactPage(BaseClass):
    def __init__(self,page):
        super().__init__(page)
        

        # Page Locators
        self.salutation_dropdown = page.locator('#salutation')
        self.first_name_input = page.locator('#first_name')
        self.last_name_input = page.locator('#last_name')
        self.office_phone_input = page.locator('#phone_work')
        self.mobile_phone_input = page.locator('#phone_mobile')
        self.job_title_input = page.locator('#title')
        self.department_input = page.locator('#department')
        self.account_name_input = page.locator('#account_name')
        self.select_account_button = page.locator('#btn_account_name')
        self.email_input = page.locator('input[type="email"][id*="emailAddress"], input#email1')

        # Address Fields
        self.primary_street_input = page.locator('#primary_address_street')
        self.primary_city_input = page.locator('#primary_address_city')
        self.primary_state_input = page.locator('#primary_address_state')
        self.primary_postal_input = page.locator('#primary_address_postalcode')
        self.primary_country_input = page.locator('#primary_address_country')

        #  Buttons
        self.save_button = page.locator('input#SAVE')
        self.cancel_button = page.locator('input#CANCEL')

        #  Confirmation
        self.header_text = page.locator('h2.module-title-text')
        
         # --- Action Methods using BaseClass ---

    def select_salutation(self, value: str):
        self.select_option_by_value(self.salutation_dropdown,value)

    def enter_first_name(self, first_name: str):
        self.fill(self.first_name_input, first_name)

    def enter_last_name(self, last_name: str):
        self.fill(self.last_name_input, last_name)

    def enter_office_phone(self, phone: str):
        self.fill(self.office_phone_input, phone)

    def enter_mobile_phone(self, mobile: str):
        self.fill(self.mobile_phone_input, mobile)

    def enter_job_title(self, title: str):
        self.fill(self.job_title_input, title)

    def enter_department(self, dept: str):
        self.fill(self.department_input, dept)

    def enter_account_name(self, account: str):
        self.fill(self.account_name_input, account)

    def click_select_account(self):
        self.click(self.select_account_button)

    def enter_email(self, email: str):
        self.fill(self.email_input, email)

    def click_save(self):
        self.click(self.save_button)

    def click_cancel(self):
        self.click(self.cancel_button)
    
        ''' Primary address actions methods '''    
    def enter_primary_street(self, street: str):
        self.fill(self.primary_street_input, street)

    def enter_primary_city(self, city: str):
        self.fill(self.primary_city_input, city)

    def enter_primary_state(self, state: str):
        self.fill(self.primary_state_input, state)

    def enter_primary_postal_code(self, postal_code: str):
        self.fill(self.primary_postal_input, postal_code)

    def enter_primary_country(self, country: str):
        self.fill(self.primary_country_input, country)

    def get_header_text(self) -> str:
        return self.get_text(self.header_text)
    
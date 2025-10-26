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
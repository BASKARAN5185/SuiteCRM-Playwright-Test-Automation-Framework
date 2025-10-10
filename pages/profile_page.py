from pages.base_class import BaseClass

class profile_page(BaseClass):
    '''Profile Page Locators'''
    ''' User Profile under locators'''
    USER_PROFILE_HEADER="(//div[@class='col-xs-10 col-sm-11 col-md-11'])[1]"
    USER_NAME="//div[contains(text(), 'will')]"
    USER_TYPE="(//div[@type='enum'])[1]"
    PHOTO_UPLOAD=" #photo_new > input#photo_file"
    FIRST_NAME="input[name='first_name']"
    LAST_NAME="div[field='last_name'] >input[name='last_name']"
    
    '''Employee Information under locators'''
    EMPLOYEE_STATUS="(//div[contains(text() , 'Active')])[2]"
    DEPARTMENT="div[field='department']"
    REPORT_TO="input#reports_to_name"
    DISPLAY_EMPLOYEE_RECORDS='div[field="show_on_employees"]'
    WORK_PHONE="input[name='phone_work']"
    MOBILE="input[name='phone_mobile']"
    OTHER_PHONE="input[name='phone_other']"
    PHONE_FAX="input[name='phone_fax']"
    HOME_PHONE='input[name="phone_home"]'
    IM_NAME='input#messenger_id'
    ADDRESS_CITY='input[name="address_city"]'
    ADDRESS_POSTAL_CODE='input[name="address_postalcode"]'
    IM_TYPE_DROPDOWN='select#messenger_type'
    ADDRESS_STREET="input#address_street"
    ADDRESS_STATE="input#address_state"
    ADDRESS_COUNTRY="input#address_country"
    DESCRIPTION='textarea'
    
    '''Email Settings under locators'''
    EMAIL_ADDRESS_ADD_BUTTON="button.btn.btn-danger.email-address-add-button"
    EMAIL_ADDRESS_REMOVE_BUTTON="button#Users0removeButton0"
    EMAIL_PRIMARY_RADIO_BUTTON='input[type="radio"][name="Users0emailAddressPrimaryFlag"]'
    EMAIL_REPLAY_TO_CHECKBOX='input[type="checkbox"][name="Users0emailAddressReplyToFlag"]'   
    EMAIL_CLIENT_DROPDOWN="[name='email_link_type']"
    EMAIL_EDITOR_DROPDOWN="[name='editor_type']" 
    
    '''Profile Page Footer Buttons locators'''
    SETTINGS_BUTTON="//button[contains(@class,'button')]//img[contains(@src,'setting')]"
    FOOTER_SAVE_BUTTON='#SAVE_FOOTER'
    FOOTER_CANCEL_BUTTON='input#CANCEL_FOOTER'
    FOOTER_RESET_USER_PREFERENCES='#reset_user_preferences_footer'
    FOOTER_RESET_HOMEPAGE='#reset_homepage_footer'
    
    '''Profile Page Header Buttons Locators'''
    HEADER_SAVE_BUTTON='#SAVE_HEADER'
    HEADER_CANCEL_BUTTON='input#CANCEL_HEADER'
    HEADER_RESET_USER_PREFERENCES='#reset_user_preferences_header'
    HEADER_RESET_HOMEPAGE='#reset_homepage_header'
    
    '''User Profile Tab Locators'''
    PROFILE_PAGE_TITLE='//a[text()="Will Westin"]'
    USER_PROFILE_TAB='a#tab1'
    ADVANCED_TAB='a#tab2'
    EXTERNAL_ACCOUNTS_TAB='a#tab3'
    LAYOUT_OPTIONS_TAB='a#tab4'
    
    '''User Profile Section acton method'''
    def user_profilesection_visible(self) -> bool:
        self.is_visible(self.USER_PROFILE_HEADER)
    
    def user_profile_section_click(self):
        self.click(self.USER_PROFILE_HEADER)
        
    def user_name_visible(self):
        self.is_visible(self.USER_NAME)
        
    def user_type_selction_visible(self):
        self.is_visible(self.USER_TYPE)
    
    def upload_photo(self,file:str):
        self.upload_file(file)
        
    def first_name_enter(self,name:str):    
        self.type_text(self.USER_NAME,name)
        
    def last_namee_enter(self,lastname:str):
        self.type_text(self.LAST_NAME,lastname)   
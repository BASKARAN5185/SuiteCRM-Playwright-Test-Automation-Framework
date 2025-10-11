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
    
    '''Email Settings section locators'''
    EMAIL_SETTING_HEADER='h4[text="Email Settings"]'
    EMAIL_ADDRESS_ADD_BUTTON="button.btn.btn-danger.email-address-add-button"
    EMAIL_ADDRESS_REMOVE_BUTTON="button#Users0removeButton0"
    EMAIL_PRIMARY_RADIO_BUTTON='input[type="radio"][name="Users0emailAddressPrimaryFlag"]'
    EMAIL_REPLAY_TO_CHECKBOX='input[type="checkbox"][name="Users0emailAddressReplyToFlag"]'   
    EMAIL_CLIENT_DROPDOWN="[name='email_link_type']"
    EMAIL_EDITOR_DROPDOWN="[name='editor_type']" 
    EMAIL_INPUT_FIELD='input[type="email"]'
    
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
    
    '''Employee Information Section action methods''' 
    def employee_information_section_visible(self) -> bool:
        self.is_visible(self.EMPLOYEE_STATUS)   
        
    def employee_information_section_click(self):
        self.click(self.EMPLOYEE_STATUS)        

    def employee_status_selection_visible(self):
        self.is_visible(self.EMPLOYEE_STATUS)
     
    def department_selection_visible(self):
        self.is_visible(self.DEPARTMENT)
        
    def report_to_enter(self,reportto:str):
        self.type_text(self.REPORT_TO,reportto)
        
    def display_employee_records_selection_visible(self):
        self.is_visible(self.DISPLAY_EMPLOYEE_RECORDS)
        
    def work_phone_enter(self,workphone:str):
        self.type_text(self.WORK_PHONE,workphone)
    
    def mobile_enter(self,mobile:str) :                     
        self.type_text(self.MOBILE,mobile)
    
    def other_phone_enter(self,otherphone:str):
        self.type_text(self.OTHER_PHONE,otherphone)
       
    def phone_fax_enter(self,phonefax:str):
        self.type_text(self.PHONE_FAX,phonefax)
        
    def home_phone_enter(self,homephone:str):
        self.type_text(self.HOME_PHONE,homephone)
    
    def im_name_enter(self,imname:str):
        self.type_text(self.IM_NAME,imname)
       
    def im_type_selection_visible(self):
        self.is_visible(self.IM_TYPE_DROPDOWN)
    
    def im_type_option_selection(self,value:str):
        self.select_option_by_value(self.IM_TYPE_DROPDOWN,value)
        
    def address_street_enter(self,addressstreet:str):
        self.type_text(self.ADDRESS_STREET,addressstreet)         
                 
    def address_city_enter(self,addresscity:str):
        self.type_text(self.ADDRESS_CITY,addresscity)
        
    def address_state_enter(self,addressstate:str):
        self.type_text(self.ADDRESS_STATE,addressstate)
    
    def address_podtal_code_enter(self,addresspostalcode:str):
        self.type_text(self.ADDRESS_POSTAL_CODE,addresspostalcode) 
        
    def address_country_enter(self,addresscountry:str):
        self.type_text(self.ADDRESS_COUNTRY,addresscountry)
        
    def description_enter(self,description:str):
        self.type_text(self.DESCRIPTION,description)
        
    ''' Email setting section action methods'''
    def email_setting_section_visible(self) -> bool:
        return self.is_visible(self.EMAIL_SETTING_HEADER)
    
    def email_address_add_button_visible(self)-> bool:
        return self.is_visible(self.EMAIL_ADDRESS_ADD_BUTTON)
    
    def email_address_add_button_click(self):
        self.click(self.EMAIL_ADDRESS_ADD_BUTTON)

    def  email_address_remove_button_visible(self) -> bool:
         return self.is_visible(self.EMAIL_ADDRESS_REMOVE_BUTTON) 
         
    def email_address_remove_button_click(self):
        self.click(self.EMAIL_ADDRESS_REMOVE_BUTTON)
    
    def email_address_primary_raido_button_click(self,index:int) -> bool:              
        radio_button=self.EMAIL_PRIMARY_RADIO_BUTTON.nth(index)
        if self.radio_uncheckbox(radio_button) :
            return self.radio_checkbox(radio_button)        
    
    def email_replayto_ckecked(self,index:int) ->bool:
        checkbox=self.EMAIL_REPLAY_TO_CHECKBOX.nth(index)
        if self.uncheck_checkbox(checkbox):
            return self.check_checkbox(checkbox)
    
    def email_client_selection(self,email:str):
        self.select_option_by_value(self.EMAIL_CLIENT_DROPDOWN,email)
        
    def email_editor_selection(self,editor:str):
        self.select_option_by_value(self.EMAIL_EDITOR_DROPDOWN,editor) 
           
    def email_input_field_visible(self,index:int) -> bool:
        email_input=self.EMAIL_INPUT_FIELD.nth(index)
        return self.is_visible(email_input)
    
    def new_mailid_enter(self,mail:str,index:int):
        email_field=self.EMAIL_INPUT_FIELD.nth(index)
        self.type_text(email_field,mail)
    
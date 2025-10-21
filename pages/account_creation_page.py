from pages.base_class import BaseClass


class account_creation_page(BaseClass):
   ''' Billing Address Locators '''
   BILLING_STREET = "#billing_address_street"
   BILLING_CITY = "#billing_address_city"
   BILLING_STATE = "#billing_address_state"
   BILLING_POSTAL_CODE = "#billing_address_postalcode"
   BILLING_COUNTRY = "#billing_address_country"

   ''' Shipping Address Locators '''
   SHIPPING_STREET = "#shipping_address_street"
   SHIPPING_CITY = "#shipping_address_city"
   SHIPPING_STATE = "#shipping_address_state"
   SHIPPING_POSTAL_CODE = "#shipping_address_postalcode"
   SHIPPING_COUNTRY = "#shipping_address_country"
   SHIPPING_COPY_CHECKBOX = "#shipping_checkbox"

   ''' Account Info Locators '''
   ACCOUNT_TYPE = "#account_type"
   INDUSTRY = "#industry"
   ANNUAL_REVENUE = "#annual_revenue"
   EMPLOYEES = "#employees"
   DESCRIPTION = "#description"

   ''' Assigned User Section Locators '''
   ASSIGNED_USER_NAME_INPUT = "input#assigned_user_name"
   ASSIGNED_USER_SELECT_BUTTON = "button#btn_assigned_user_name"
   ASSIGNED_USER_CLEAR_BUTTON = "button#btn_clr_assigned_user_name"

   ''' Parent Account Field Locators '''
   PARENT_NAME_INPUT = "input#parent_name"
   PARENT_SELECT_BUTTON = "button#btn_parent_name"
   PARENT_CLEAR_BUTTON = "button#btn_clr_parent_name"

   ''' Campaign Field Locators '''
   CAMPAIGN_NAME_INPUT = "input#campaign_name"
   CAMPAIGN_SELECT_BUTTON = "button#btn_campaign_name"
   CAMPAIGN_CLEAR_BUTTON = "button#btn_clr_campaign_name"

   ''' Account Creation Buttons '''
   SAVE_BUTTON = "button#SAVE"
   CANCEL_BUTTON = "button#CANCEL"
   EDIT_FORM = "#EditView"

   ''' billing address section locators '''
   def enter_billing_street(self, street):
       self.type_text(self.BILLING_STREET, street)

   def enter_billing_city(self, city):
       self.type_text(self.BILLING_CITY, city)
       
   def enter_billing_state(self, state):
         self.type_text(self.BILLING_STATE, state) 
               
   def enter_billing_postal_code(self, postal_code):
       self.type_text(self.BILLING_POSTAL_CODE, postal_code)      
   
   def enter_billing_country(self, country):
       self.type_text(self.BILLING_COUNTRY, country)
       
   ''' shipping address section locators '''
   def enter_shipping_street(self, street):   
       self.type_text(self.SHIPPING_STREET, street)
       
   def enter_shipping_city(self, city):
       self.type_text(self.SHIPPING_CITY, city)
       
   def enter_shipping_state(self, state):
       self.type_text(self.SHIPPING_STATE, state)
       
   def enter_shipping_postal_code(self, postal_code):
       self.type_text(self.SHIPPING_POSTAL_CODE, postal_code)
       
   def enter_shipping_country(self, country):
         self.type_text(self.SHIPPING_COUNTRY, country)
   
   def click_shipping_copy_checkbox(self):
       self.click_element(self.SHIPPING_COPY_CHECKBOX)
           
   def billing_section(self, street, city, state, postal_code, country):
       self.enter_billing_street(street)
       self.enter_billing_city(city)
       self.enter_billing_state(state)
       self.enter_billing_postal_code(postal_code)
       self.enter_billing_country(country)
       
   def shipping_section(self, street, city, state, postal_code, country):
       self.enter_shipping_street(street)
       self.enter_shipping_city(city)
       self.enter_shipping_state(state)
       self.enter_shipping_postal_code(postal_code)
       self.enter_shipping_country(country)           
       
       ''' account info section action methods '''
   def  accoun_type(self,type:str):
        self.select_option_by_value(self.ACCOUNT_TYPE,type)
        
   def industry(self,industry:str):
        self.select_option_by_value(self.INDUSTRY,industry)
             
   def annual_revenue(self,revenue:str):
        self.type_text(self.ANNUAL_REVENUE,revenue)
        
   def employees(self,employees:str):
           self.type_text(self.EMPLOYEES,employees)
    
   def description(self,description:str):
        self.type_text(self.DESCRIPTION,description)
     
   ''' assigned user section action methods '''
   def assigned_user_name(self,user_name:str):
        self.type_text(self.ASSIGNED_USER_NAME_INPUT,user_name)
        
   def click_assigned_user_select_button(self):
        self.click(self.ASSIGNED_USER_SELECT_BUTTON)                                      
        
   def click_assigned_user_clear_button(self):
        self.click(self.ASSIGNED_USER_CLEAR_BUTTON)
        
   ''' parent account section action methods '''
   def parent_name(self,parent_name:str):
        self.type_text(self.PARENT_NAME_INPUT,parent_name)
        
   def click_parent_select_button(self):
        self.click(self.PARENT_SELECT_BUTTON)
    
   def click_parent_clear_button(self):
        self.click(self.PARENT_CLEAR_BUTTON)
    
        ''' campaign section action methods ''' 
   def campaign_name(self,campaign_name:str):  
        self.type_text(self.CAMPAIGN_NAME_INPUT,campaign_name)
   
   def click_campaign_select_button(self):
        self.click(self.CAMPAIGN_SELECT_BUTTON)
    
   def click_campaign_clear_button(self):
        self.click(self.CAMPAIGN_CLEAR_BUTTON)
    
        ''' account creation buttons action methods '''    
   def click_save_button(self):
        self.click(self.SAVE_BUTTON)
    
   def click_cancel_button(self):
        self.click(self.CANCEL_BUTTON)
    
   def is_edit_form_displayed(self) -> bool:       
        return self.is_element_visible(self.EDIT_FORM)                              
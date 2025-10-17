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

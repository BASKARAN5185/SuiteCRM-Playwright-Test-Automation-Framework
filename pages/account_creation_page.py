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



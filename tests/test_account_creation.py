from pages.account_creation_page import account_creation_page
import pytest

@pytest.fixture('scope=function')
def test_account_creation_page_navigation(page):
    account_page = account_creation_page(page)
    page.goto('https://demo.suiteondemand.com/index.php?module=Accounts&action=EditView&return_module=Accounts&return_action=DetailView')
    assert page.locator(account_page.EDIT_FORM).is_visible(), "Account Creation page did not load properly"

@pytest.mark.smoke
@pytest.mark.accountcreationpage
@pytest.mark.parametrize("street, city, state, postal_code, country", [
    ("123 Main St", "Springfield", "IL", "62701", "USA"),
    ("456 Elm St", "Metropolis", "NY", "10001", "USA"),
    ("789 Oak St", "Gotham", "NJ", "07097", "USA"),
    ('101 Pine St', "Smallville", "KS", "66002", "USA"),
    ('','','','','')
])
def test_enter_billing_address(test_account_creation_page_navigation, street, city, state, postal_code, country):
    account_page = account_creation_page(test_account_creation_page_navigation)
    account_page.billing_section(street, city, state, postal_code, country)
    assert test_account_creation_page_navigation.locator(account_page.BILLING_STREET).input_value() == street,'street does not match'
    assert test_account_creation_page_navigation.locator(account_page.BILLING_CITY).input_value() == city,'city does not match'
    assert test_account_creation_page_navigation.locator(account_page.BILLING_STATE).input_value() == state,'state value does not match'
    assert test_account_creation_page_navigation.locator(account_page.BILLING_POSTAL_CODE).input_value() == postal_code,'postal code does not match'
    assert test_account_creation_page_navigation.locator(account_page.BILLING_COUNTRY).input_value() == country,'country does not match'    

@pytest.param("'street''city''state''postalcode''country'", [
    ('nortt strret','new york','ny','100001','usa'),
    ('southern','los angeles','ca','90001','usa')     
    ('eastern','miami','fl','33101','usa'),
    ('western','seattle','wa','98101','usa'),
    ('','','','','')])    
def test_enter_shoping_address(test_account_creation_page_navigation : account_creation_page ,street,city,state,postalcode,country):
    account_page =account_creation_page(test_account_creation_page_navigation)
    account_page.shipping_section(street,city,state,postalcode,country)  
    assert test_account_creation_page_navigation.locator(account_page.SHIPPING_STREET).input_value() == street ,'street does not match'
    assert test_account_creation_page_navigation.SHIPPING_CITY.input_value() == city,'city does not match'
    assert test_account_creation_page_navigation.SHIPPING_STATE.input_value() == state,'state does not match'
    assert test_account_creation_page_navigation.SHIPPING_POSTAL_CODE.input_value() == postalcode,'postal code does not match'   
    assert test_account_creation_page_navigation.SHIPPING_COUNTRY.input_value() == country,'country does not match'

@pytest.mark.smoke
@pytest.mark.accountcreationpage
@pytest.param("'actype' 'revenue' 'employee' 'description' 'industry'",[(1,'10000','karthik','Manger','IT')])
def test_enter_account_info(test_account_creation_page_navigation : account_creation_page,actype,revenue,employee,description,industry):
    account_page=account_creation_page(test_account_creation_page_navigation)
    account_page.accoun_type(actype)
    account_page.annual_revenue(revenue)
    account_page.employees(employee)
    account_page.description(description)
    account_page.industry(industry)
    assert account_creation_page.ACCOUNT_TYPE.input_value() == actype ,"account type does not match"
    assert account_creation_page.ANNUAL_REVENUE.input_value() == revenue ,"revenue does not match"
    assert account_creation_page.EMPLOYEES.input_value() == employee ,"employee type does not match"
    assert account_creation_page.DESCRIPTION.input_value() == description ,"account type does not match"
    assert account_creation_page.INDUSTRY.input_value() == industry ,"account type does not match"
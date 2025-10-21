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
    assert test_account_creation_page_navigation.locator(account_page.BILLING_STREET).input_value() == street
    assert test_account_creation_page_navigation.locator(account_page.BILLING_CITY).input_value() == city
    assert test_account_creation_page_navigation.locator(account_page.BILLING_STATE).input_value() == state
    assert test_account_creation_page_navigation.locator(account_page.BILLING_POSTAL_CODE).input_value() == postal_code
    assert test_account_creation_page_navigation.locator(account_page.BILLING_COUNTRY).input_value() == country    
    

    
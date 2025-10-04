from playwright.sync_api import expect 
from pages.login_page import LoginPage
import pytest

@pytest.fixture(scope='function')
def go_to_login_page(page):
    page.goto('https://demo.suiteondemand.com/index.php?action=Login&module=Users')
    yield page

@pytest.fixture(scope='function')
def perform_login(page):
    page.goto('https://demo.suiteondemand.com/index.php?action=Login&module=Users')
    page.locator('#user_name').fill('will')
    page.locator('#username_password').fill('will')
    page.locator('#bigbutton').click()
    # wait for navigation or success indication here
    page.wait_for_load_state('networkidle')
    yield page

@pytest.fixture(scope='function')
def login(perform_login):
    page=perform_login
    # Now the page should be logged in and navigated to the welcome screen
    welcome_message = page.get_by_text('Welcome to the SuiteCRM 7 Demo')
    expect(welcome_message).to_be_visible(timeout=10000)  # wait up to 10 seconds
    assert welcome_message.is_visible()
    login_page = LoginPage(page)
    return login_page

@pytest.mark.ragression
def test_header_logo_visible(go_to_login_page):
    login=LoginPage(go_to_login_page)
    assert login.header_logo_is_visible() , 'Header logo is not visible'

@pytest.mark.smoke
def test_company_logo_visble(go_to_login_page):
    login=LoginPage(go_to_login_page)
    assert login.company_logo_is_visible() , 'Comapny logo is not visible' 

@pytest.mark.sanity
def test_Home_craeate_button_visible(login):
    assert login.is_home_page_text_visible() , 'Home page navigtion is failed '
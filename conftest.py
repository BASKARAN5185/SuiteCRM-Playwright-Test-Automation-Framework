import pytest
from playwright.sync_api import sync_playwright ,Page

@pytest.fixture(scope='session')
def playwright_instance():
    playwright = sync_playwright().start()
    yield playwright
    playwright.stop()
    
@pytest.fixture(scope='session')
def browser(playwright_instance)  :
    browser=playwright_instance.chromium.launch(headless=False)
    yield browser
    browser.close()
    
@pytest.fixture(scope='function') 
def page(browser)->Page:
    context=browser.new_context()
    page=context.new_page()
    yield page
    context.close()
    
@pytest.fixture(scope='function')
def perform_login(page):
    page.goto('https://demo.suiteondemand.com/index.php?action=Login&module=Users')
    page.locator('#user_name').fill('will')
    page.locator('#username_password').fill('will')
    page.locator('#bigbutton').click()
    yield
       
       
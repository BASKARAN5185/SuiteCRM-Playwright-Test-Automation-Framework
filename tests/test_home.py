from pages.home_page import HomePage
from playwright.sync_api import expect
import pytest

@pytest.fixture(scope='function')
def perform_login(page):
    page.goto('https://demo.suiteondemand.com/index.php?action=Login&module=Users')
    page.locator('#user_name').fill('will')
    page.locator('#username_password').fill('will')
    page.locator('#bigbutton').click()
    # wait for navigation or success indication here
    page.wait_for_load_state('networkidle')
    yield page 
    return page

@pytest.mark.sanity
def test_user_icon_visible(perform_login):
    home=HomePage(perform_login)
    assert home.user_icon_visible() , 'User icon is not visible'

@pytest.mark.sanity
def test_notification_icon_visible(perform_login):
    home=HomePage(perform_login)
    assert home.notification_icon_visible() , 'Notification icon is not visible'

@pytest.mark.sanity
def test_search_button_visible(perform_login):
    home=HomePage(perform_login)
    assert home.search_button_visible() , 'Search button is not visible'

@pytest.mark.sanity
def test_search_textbox_visible(perform_login): 
    home=HomePage(perform_login)
    assert home.seaerch_textbox_visible() , 'Search textbox is not visible'

@pytest.mark.sanity
def test_search_textbox_fill(perform_login):
    home=HomePage(perform_login)
    home.search_textbox_fill('test')
    assert home.get_value(home.SEARCH_TEXTBOX)=='test' , 'Search textbox fill is not working'

@pytest.mark.sanity
def test_create_button_click(perform_login):
    home=HomePage(perform_login)
    home.create_click()
    assert home.get_title()=='Create' , 'Create button click is not working'

@pytest.mark.sanity
def test_home_icon_click(perform_login):
    home=HomePage(perform_login)
    home.home_icon_click()
    assert home.get_title()=='Home' , 'Home icon click is not working'

@pytest.mark.sanity
def test_sales_menu_click(perform_login):   
    home=HomePage(perform_login)
    home.sales_menu_click()
    assert home.get_title()=='Sales' , 'Sales menu click is not working'

@pytest.mark.sanity
def test_marketing_menu_click(perform_login):
    home=HomePage(perform_login)
    home.marketing_menu_click()
    assert home.get_title()=='Marketing' , 'Marketing menu click is not working'

@pytest.mark.sanity
def test_support_menu_click(perform_login): 
    home=HomePage(perform_login)
    home.support_menu_click()
    assert home.get_title()=='Support' , 'Support menu click is not working'

@pytest.mark.sanity
def test_activities_menu_click(perform_login):              
    home=HomePage(perform_login)
    home.activities_menu_click()
    assert home.get_title()=='Activities' , 'Activities menu click is not working'

@pytest.mark.sanity
def test_collabration_menu_click(perform_login):        
    home=HomePage(perform_login)
    home.collabration_menu_click()
    assert home.get_title()=='Collabration' , 'Collabration menu click is not working'

@pytest.mark.sanity
def test_all_menu_click(perform_login):        
    home=HomePage(perform_login)
    home.all_menu_click()
    assert home.get_title()=='All' , 'All menu click is not working'

@pytest.mark.sanity
def test_user_icon_click(perform_login):
    home=HomePage(perform_login)
    home.user_icon_click()
    profile_option=home.page.get_byRole("menuitem", name="Profile")
    expect(profile_option).to_be_visible(timeout=5000)
    assert profile_option.is_visible() , 'User icon click is not working'

@pytest.mark.sanity
def test_notification_icon_click(perform_login):
    home=HomePage(perform_login)
    home.notification_icon_click()
    notification_header=home.page.get_byText("Notifications")
    expect(notification_header).to_be_visible(timeout=5000)
    assert notification_header.is_visible() , 'Notification icon click is not working'

@pytest.mark.sanity
def test_search_button_click(perform_login):
    home=HomePage(perform_login)
    home.search_button_click()
    search_results=home.page.get_byText("Search Results")
    expect(search_results).to_be_visible(timeout=5000)
    assert search_results.is_visible() , 'Search button click is not working'

@pytest.mark.sanity 
def test_get_title(perform_login):
    home=HomePage(perform_login)
    assert home.get_title()=='Home' , 'Title is not matching'

@pytest.mark.sanity
def test_get_url(perform_login):
    home=HomePage(perform_login)
    assert home.get_url()=='https://demo.suiteondemand.com/index.php?module=Home&action=index' , 'URL is not matching'


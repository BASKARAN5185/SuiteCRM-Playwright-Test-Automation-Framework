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

@pytest.mark.retest
def test_user_icon_visible(perform_login):
    home=HomePage(perform_login)
    assert home.user_icon_visible() , 'User icon is not visible'

@pytest.mark.somke
def test_notification_icon_visible(perform_login):
    home=HomePage(perform_login)
    assert home.notification_icon_visible() , 'Notification icon is not visible'

@pytest.mark.smoke
def test_search_button_visible(perform_login):
    home=HomePage(perform_login)
    assert home.search_button_visible() , 'Search button is not visible'

@pytest.mark.smoke
def test_create_button_click(perform_login):
    home=HomePage(perform_login)
    home.create_button_visible_and_click()
    home.Create_account_dropdown_click()
    assert 'Accounts&return_action' in home.get_url(), "Create Account Page naviagtion is not working "
    
@pytest.mark.smoke
def test_home_icon_click(perform_login):
    home=HomePage(perform_login)
    home.home_icon_click()
    assert 'index' in home.get_url(), 'Home icon click is not working'

@pytest.mark.smoke
def test_sales_menu_dropdown(perform_login):   
    home = HomePage(perform_login)
    home.sales_menu_over()
    home.home_dropdown_click(1)
    assert 'Sales' in home.get_url(), 'Sales drop down menu home page navigation is not working'

@pytest.mark.smoke
def test_marketing_menu_dropdown(perform_login):
    home = HomePage(perform_login)
    home.marketing_menu_over()
    home.home_dropdown_click(2)
    assert 'Marketing' in home.get_url(), 'Marketing drop down menu home page navigation is not working'

@pytest.mark.smoke
def test_support_menu_dropdown(perform_login): 
    home = HomePage(perform_login)
    home.support_menu_over()
    home.home_dropdown_click(3)
    assert 'Support' in home.get_url(), 'Support drop down menu home page navigation is not working'

@pytest.mark.smoke
def test_activities_menu_dropdown(perform_login):              
    home = HomePage(perform_login)
    home.activities_menu_over()
    home.home_dropdown_click(4)
    assert 'Activities' in home.get_url(), 'Activities drop down menu home page navigation is not working'

@pytest.mark.smoke
def test_collaboration_menu_dropdown(perform_login):        
    home = HomePage(perform_login)
    home.collaboration_menu_over()
    home.home_dropdown_click(5)
    assert 'Collaboration' in home.get_url(), 'Collaboration drop down menu home page navigation is not working'

@pytest.mark.smoke
def test_all_menu_dropdown(perform_login):        
    home = HomePage(perform_login)
    home.all_menu_over()
    home.home_dropdown_click(6)
    assert 'All' in home.get_url(), 'All drop down menu home page navigation is not working'
    
@pytest.mark.skip
def test_user_icon_click(perform_login):
    home=HomePage(perform_login)
    home.user_icon_click()
    assert home.user_icon_click()
    
@pytest.mark.skip
def test_notification_icon_click(perform_login):
    home=HomePage(perform_login)
    home.notification_icon_visible()
    assert home.notification_icon_click()

@pytest.mark.skip
def test_search_box_validation(perform_login):
    home=HomePage(perform_login)
    home.search_button_click()
    assert home.search_textbox_visible() , 'Search box is not visible'
    home.search_textbox_fill("loss innocence")
    home.search_input_box_button_click()
    assert "loss innocence" in home.get_url(), "search filter is not working properly"

@pytest.mark.smoke
def test_get_url(perform_login):
    home=HomePage(perform_login)
    assert home.get_url()=='https://demo.suiteondemand.com/index.php?module=Home&action=Demo' , 'URL is not matching'


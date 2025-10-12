from pages.profile_page import ProfilePage
import pytest

@pytest.fixture(scope='function')
def go_to_login_with_profile(page):
    page.goto('https://demo.suiteondemand.com/index.php?action=Login&module=Users')
    page.locator('#user_name').fill('will')
    page.locator('#username_password').fill('will')
    page.locator('#bigbutton').click()  
    page.wait_for_load_state('networkidle')
    page.locator('text=Welcome to the SuiteCRM 7 Demo').click()
    page.goto('https://demo.suiteondemand.com/index.php?module=Users&action=EditView&record=seed_will_id')
    page.wait_for_load_state('networkidle')
    
    profile = ProfilePage(page)
    yield profile

@pytest.mark.profilepage
@pytest.mark.sanity
def test_profile_tab_visible(go_to_login_with_profile: ProfilePage):
    profile = go_to_login_with_profile
    profile.user_profilesection_visible(), 'Profile page navigation is faield'

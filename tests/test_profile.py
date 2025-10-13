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
@pytest.mark.smoke
def test_profile_tab_visible(go_to_login_with_profile: ProfilePage):
    profile = go_to_login_with_profile
    profile.user_profilesection_visible(), 'Profile page navigation is faield'

@pytest.mark.profilepage
@pytest.mark.sanity1
def test_update_user_profile(go_to_login_with_profile: ProfilePage):
    profile = go_to_login_with_profile
    profile.first_name_enter('william')
    profile.last_namee_enter('smith')
    profile.upload_photo('C:/Users/ELCOT/Downloads/git progile.png')
    profile.header_save_button_click()
    assert 'william' in profile.get_attribute(profile.FIRST_NAME,'value'), 'First name not updated'
    assert 'smith' in profile.get_attribute(profile.LAST_NAME,'value'), 'Last name not updated'
    assert profile.is_visible(profile.PHOTO_UPLOAD), 'Profile photo not updated'
    
@pytest.mark.profilepage
@pytest.mark.sanity1
def test_cancel_user_profile_update(go_to_login_with_profile: ProfilePage):
    profile = go_to_login_with_profile
    profile.first_name_enter('william')
    profile.last_namee_enter('smith')
    profile.upload_photo('C:/Users/ELCOT/Downloads/git progile.png')
    profile.header_cancel_button_click()
    assert 'will' in profile.get_attribute(profile.USER_NAME,'value'), 'First name updated'
    assert 'chris' in profile.get_attribute(profile.LAST_NAME,'value'), 'Last name updated'
    assert not profile.is_visible(profile.PHOTO_UPLOAD), 'Profile photo updated'    
    
@pytest.mark.profilepage
@pytest.mark.sanity1
def test_last_name_empty_validation(go_to_login_with_profile:ProfilePage):
    profile = go_to_login_with_profile
    profile.first_name_enter('william')
    profile.last_namee_enter('')
    profile.header_save_button_click()
    assert 'william' in profile.get_attribute(profile.USER_NAME,'value'), 'last name empty validation failed'

@pytest.mark.profilepage
@pytest.ark.sanity1
def test_user_name_non_editable(go_to_login_with_profile:ProfilePage):
    profile = go_to_login_with_profile
    assert profile.get_attribute(profile.USER_NAME,'disabled') is not None, 'User name field is editable'
    
@pytest.mark.profilepage
@pytest.mark.sanity1
def test_profile_staus_non_editable(go_to_login_with_profile:ProfilePage):
    profile = go_to_login_with_profile
    assert profile.get_attribute(profile.STATUS,'disabled') is not None, 'Status field is editable'

@pytest.mark.profilepage
@pytest.mark.sanity1
def test_user_type_non_editable(go_to_login_with_profile:ProfilePage):
    profile = go_to_login_with_profile
    assert profile.get_attribute(profile.USER_TYPE,'disabled') is not None, 'User type field is editable'
           
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

''' Profile Page Navigation & Visibility Tests '''
@pytest.mark.profilepage
@pytest.mark.smoke
def test_profile_tab_visible(go_to_login_with_profile: ProfilePage):
    profile = go_to_login_with_profile
    profile.user_profilesection_visible(), 'Profile page navigation is faield'

''' User Profile page section visibility & field editability tests '''

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
    
@pytest.mark.profilepage
@pytest.mark.sanity1
def test_employee_information_section_visible(go_to_login_with_profile:ProfilePage):
    profile = go_to_login_with_profile
    profile.employee_information_section_visible(), 'Employee information section not visible'    
    
''' Profile Update & Cancel Tests '''

@pytest.mark.profilepage
@pytest.mark.sanity1    
def test_update_employee_information(go_to_login_with_profile: ProfilePage):
    profile = go_to_login_with_profile
    profile.employee_status_selection_visible()
    profile.department_selection_visible()
    profile.report_to_enter('will')
    profile.display_employee_records_selection_visible()
    profile.work_phone_enter('1234567890')
    profile.mobile_enter('9876543210')
    profile.other_phone_enter('1231231234')
    profile.phone_fax_enter('4564564567')
    profile.home_phone_enter('7897897890')
    profile.im_name_enter('willim')
    profile.address_city_enter('chennai')
    profile.address_state_enter('tamilnadu')
    profile.address_podtal_code_enter('600119')
    profile.address_country_enter('india')
    profile.address_street_enter('no:12,abc street')
    profile.im_type_selection_visible()
    profile.im_type_option_selection('AOL')
    profile.description_enter('hello everyone')
    profile.header_save_button_click()

    assert '1234567890' in profile.get_attribute(profile.WORK_PHONE, 'value')
    assert '9876543210' in profile.get_attribute(profile.MOBILE, 'value')
    assert '1231231234' in profile.get_attribute(profile.OTHER_PHONE, 'value')
    assert '4564564567' in profile.get_attribute(profile.PHONE_FAX, 'value')
    assert '7897897890' in profile.get_attribute(profile.HOME_PHONE, 'value')
    assert 'willim' in profile.get_attribute(profile.IM_NAME, 'value')
    assert 'chennai' in profile.get_attribute(profile.ADDRESS_CITY, 'value')
    assert 'tamilnadu' in profile.get_attribute(profile.ADDRESS_STATE, 'value')
    assert '600119' in profile.get_attribute(profile.ADDRESS_POSTAL_CODE, 'value')
    assert 'india' in profile.get_attribute(profile.ADDRESS_COUNTRY, 'value')
    assert 'no:12,abc street' in profile.get_attribute(profile.ADDRESS_STREET, 'value')
    assert 'AOL' in profile.get_attribute(profile.IM_TYPE_DROPDOWN, 'value')
    assert 'hello everyone' in profile.get_attribute(profile.DESCRIPTION, 'value')

@pytest.mark.profilepage
@pytest.mark.sanity1
def test_cancel_employee_information_update(go_to_login_with_profile: ProfilePage):
    profile = go_to_login_with_profile
    profile.employee_status_selection_visible()
    profile.department_selection_visible()
    profile.report_to_enter('will')
    profile.display_employee_records_selection_visible()
    profile.work_phone_enter('1234567890')
    profile.mobile_enter('9876543210')
    profile.other_phone_enter('1231231234')
    profile.phone_fax_enter('4564564567')
    profile.home_phone_enter('7897897890')
    profile.im_name_enter('willim')
    profile.address_city_enter('chennai')
    profile.address_state_enter('tamilnadu')
    profile.address_podtal_code_enter('600119')
    profile.address_country_enter('india')
    profile.address_street_enter('no:12,abc street')
    profile.im_type_selection_visible()
    profile.im_type_option_selection('AOL')
    profile.description_enter('hello everyone')
    profile.header_cancel_button_click()

    assert '5555555555' in profile.get_attribute(profile.WORK_PHONE, 'value')
    assert '4444444444' in profile.get_attribute(profile.MOBILE, 'value')
    assert '3333333333' in profile.get_attribute(profile.OTHER_PHONE, 'value')
    assert '2222222222' in profile.get_attribute(profile.PHONE_FAX, 'value')
    assert '1111111111' in profile.get_attribute(profile.HOME_PHONE, 'value')
    assert 'will' in profile.get_attribute(profile.IM_NAME, 'value')
    assert 'chris' in profile.get_attribute(profile.ADDRESS_CITY, 'value')
    assert 'california' in profile.get_attribute(profile.ADDRESS_STATE, 'value')
    assert '90001' in profile.get_attribute(profile.ADDRESS_POSTAL_CODE, 'value')
    assert 'usa' in profile.get_attribute(profile.ADDRESS_COUNTRY, 'value')
    assert '123 main street' in profile.get_attribute(profile.ADDRESS_STREET, 'value')
    assert '' in profile.get_attribute(profile.IM_TYPE_DROPDOWN, 'value')
    assert 'test user' in profile.get_attribute(profile.DESCRIPTION, 'value')

''' Empty Field Validations (Parameterized) '''

@pytest.mark.profilepage
@pytest.mark.sanity1
@pytest.mark.parametrize("field_method, attr, expected_value", [
    ('report_to_enter', 'REPORT_TO', 'will'),
    ('work_phone_enter', 'WORK_PHONE', '5555555555'),
    ('mobile_enter', 'MOBILE', '4444444444'),
    ('other_phone_enter', 'OTHER_PHONE', '3333333333'),
    ('phone_fax_enter', 'PHONE_FAX', '2222222222'),
    ('home_phone_enter', 'HOME_PHONE', '1111111111'),
    ('im_name_enter', 'IM_NAME', 'will'),
    ('address_city_enter', 'ADDRESS_CITY', 'chris'),
    ('address_state_enter', 'ADDRESS_STATE', 'california'),
    ('address_podtal_code_enter', 'ADDRESS_POSTAL_CODE', '90001'),
    ('address_country_enter', 'ADDRESS_COUNTRY', 'usa'),
    ('address_street_enter', 'ADDRESS_STREET', '123 main street'),
    ('description_enter', 'DESCRIPTION', 'test user'),
])
def test_empty_field_validation(go_to_login_with_profile: ProfilePage, field_method, attr, expected_value):
    profile = go_to_login_with_profile
    getattr(profile, field_method)('')
    profile.header_save_button_click()
    assert expected_value in profile.get_attribute(getattr(profile, attr), 'value')

''' Other Specific Validations '''

@pytest.mark.profilepage
@pytest.mark.sanity1
def test_display_employee_records_empty_validation(go_to_login_with_profile: ProfilePage):
    profile = go_to_login_with_profile
    profile.display_employee_records_selection_visible()
    profile.header_save_button_click()
    assert '10' in profile.get_attribute(profile.DISPLAY_EMPLOYEE_RECORDS, 'value')

@pytest.mark.profilepage
@pytest.mark.sanity1
def test_im_type_empty_validation(go_to_login_with_profile: ProfilePage):
    profile = go_to_login_with_profile
    profile.im_type_selection_visible()
    profile.im_type_option_selection('')
    profile.header_save_button_click()
    assert '' in profile.get_attribute(profile.IM_TYPE_DROPDOWN, 'value')

''' Non-editable Fields '''

@pytest.mark.profilepage
@pytest.mark.sanity1
def test_report_to_non_editable(go_to_login_with_profile: ProfilePage):
    profile = go_to_login_with_profile
    assert profile.get_attribute(profile.REPORT_TO, 'disabled') is not None

@pytest.mark.profilepage
@pytest.mark.sanity1
def test_employee_status_non_editable(go_to_login_with_profile: ProfilePage):
    profile = go_to_login_with_profile
    assert profile.get_attribute(profile.EMPLOYEE_STATUS, 'disabled') is not None

@pytest.mark.profilepage
@pytest.mark.sanity1
def test_department_non_editable(go_to_login_with_profile: ProfilePage):
    profile = go_to_login_with_profile
    assert profile.get_attribute(profile.DEPARTMENT, 'disabled') is not None

''' email section visibility & field editability tests '''

@pytest.mark.profilepage
@pytest.mark.sanity1
def test_email_section_visible(go_to_login_with_profile:ProfilePage):
    profile = go_to_login_with_profile
    profile.email_section_visible(), 'Email section not visible'
    
@pytest.mark.profilepage
@pytest.mark.sanity1
def test_email_address_section_visible(go_to_login_with_profile:ProfilePage):
    profile = go_to_login_with_profile
    profile.email_address_section_visible(), 'Email address section not visible'
    
@pytest.mark.profilepage
@pytest.mark.sanity1
def test_add_email_button_visible(go_to_login_with_profile:ProfilePage):
    profile = go_to_login_with_profile
    profile.add_email_button_visible(), 'Add email button not visible'
    
@pytest.mark.profilepage
@pytest.mark.sanity1
def test_email_setting_section_visible(go_to_login_with_profile:ProfilePage):
    profile = go_to_login_with_profile
    profile.email_setting_section_visible(), 'Email setting section not visible'                

@pytest.mark.profilepage
@pytest.mark.sanity1
def test_email_address_add_button_visible(go_to_login_with_profile:ProfilePage):
    profile = go_to_login_with_profile
    profile.email_address_add_button_visible(), 'Email address add button not visible'

@pytest.mark.profilepage
@pytest.mark.sanity1
def test_email_remove_button_visible(go_to_login_with_profile:ProfilePage):
    profile = go_to_login_with_profile
    profile.email_address_remove_button_visible(), 'Email remove button not visible'

@pytest.mark.profilepage
@pytest.mark.sanity1
def test_email_address_editable(go_to_login_with_profile:ProfilePage):
    profile = go_to_login_with_profile
    assert profile.get_attribute(profile.EMAIL_ADDRESS,'disabled') is None, 'Email address field is not editable'
    
@pytest.mark.profilepage
@pytest.mark.sanity1
def test_email_primary_non_editable(go_to_login_with_profile:Profile):
    profile = go_to_login_with_profile
    assert profile.get_attribute(profile.EMAIL_PRIMARY,'disabled') is not None, 'Email primary field is editable'
    
    
@pytest.mark.profilepage    
@pytest.mark.sanity1
def test_email_opt_out_editable(go_to_login_with_profile:ProfilePage):
    profile = go_to_login_with_profile
    assert profile.get_attribute(profile.EMAIL_OPT_OUT,'disabled') is None, 'Email opt out field is not editable'
    
@pytest.mark.profilepage
@pytest.mark.sanity1
def test_email_invalid_validation(go_to_login_with_profile:ProfilePage):
    profile = go_to_login_with_profile
    profile.email_address_enter('william')
    profile.header_save_button_click()
    assert profile.is_visible(profile.EMAIL_INVALID_MSG), 'Invalid email validation failed'

'''   Header Buttons Visibility & Functionality Tests   '''    
@pytest.mark.profilepage
@pytest.mark.sanity1
def test_header_buttons_visible(go_to_login_with_profile:ProfilePage):
    profile = go_to_login_with_profile
    profile.header_save_button_visible(), 'Header save button not visible'
    profile.header_cancel_button_visible(), 'Header cancel button not visible'
    profile.header_user_reference_button_visible(), 'Header user reference button not visible'
    profile.header_reset_homepage_button_visible(), 'Header reset homepage button not visible'

'''   Footer Buttons Visibility & Functionality Tests   '''
@pytest.mark.profilepage
@pytest.mark.sanity1
def test_footer_buttons_visible(go_to_login_with_profile:ProfilePage):
    profile = go_to_login_with_profile
    profile.footer_save_button_visible(), 'Footer save button not visible'
    profile.footer_cancel_button_visible(), 'Footer cancel button not visible'
    profile.footer_user_reference_button_visible(), 'Footer user reference button not visible'
    profile.footer_reset_homepage_button_visible(), 'Footer reset homepage button not visible'
    
@pytest.mark.profilepage
@pytest.mark.sanity1
def test_add_email_functionality(go_to_login_with_profile:ProfilePage):
    profile = go_to_login_with_profile
    initial_count = profile.EMAIL_INPUT_FIELD.count()
    profile.add_email_button_click()
    new_count = profile.EMAIL_INPUT_FIELD.count()
    assert new_count == initial_count + 1, 'Add email functionality failed'

@pytest.mark.profilepage
@pytest.mark.sanity1
def test_remove_email_functionality(go_to_login_with_profile:ProfilePage):
    profile = go_to_login_with_profile
    initial_count = profile.EMAIL_INPUT_FIELD.count()
    if initial_count > 1:
        profile.email_address_remove_button_click()
        new_count = profile.EMAIL_INPUT_FIELD.count()
        assert new_count == initial_count - 1, 'Remove email functionality failed'
    else:
        pytest.skip('Not enough email addresses to remove one')

@pytest.mark.profilepage
@pytest.mark.sanity1
def test_set_primary_email_functionality(go_to_login_with_profile:ProfilePage):
    profile = go_to_login_with_profile
    if profile.EMAIL_PRIMARY_RADIO_BUTTON.count() > 1:
        profile.email_address_primary_raido_button_click(1)
        assert profile.EMAIL_PRIMARY_RADIO_BUTTON.nth(1).is_checked(), 'Set primary email functionality failed'
    else:
        pytest.skip('Not enough email addresses to set primary')
                                   
@pytest.mark.profilepage
@pytest.mark.sanity1
def test_email_replayto_functionality(go_to_login_with_profile:ProfilePage):
    profile = go_to_login_with_profile
    if profile.EMAIL_REPLAY_TO_CHECKBOX.count() > 0:
        profile.email_replayto_ckecked(0)
        assert profile.EMAIL_REPLAY_TO_CHECKBOX.nth(0).is_checked(), 'Email reply-to functionality failed'
    else:
        pytest.skip('No email addresses available to set reply-to')    
        
@pytest.mark.profilepage
@pytest.mark.sanity1
def test_header_save_button_click(go_to_login_with_profile:ProfilePage):
    profile = go_to_login_with_profile
    profile.header_save_button_click()
    profile.page.wait_for_load_state('networkidle')
    assert profile.is_visible(profile.SUCCESS_MSG), 'Profile save operation failed'

@pytest.mark.profilepage
@pytest.mark.sanity1
def test_footer_save_button_click(go_to_login_with_profile:ProfilePage):
    profile = go_to_login_with_profile
    profile.footer_save_button_click()
    profile.page.wait_for_load_state('networkidle')
    assert profile.is_visible(profile.SUCCESS_MSG), 'Profile save operation failed'

@pytest.mark.profilepage
@pytest.mark.sanity1
def test_email_client_selection(go_to_login_with_profile:ProfilePage):
    profile = go_to_login_with_profile
    profile.email_client_selection('gmail')
    assert 'gmail' in profile.get_attribute(profile.EMAIL_CLIENT_DROPDOWN,'value'), 'Email client selection failed'             

@pytest.mark.profilepage
@pytest.mark.sanity1
def test_email_editor_selection(go_to_login_with_profile:ProfilePage):
    profile = go_to_login_with_profile
    profile.email_editor_selection('html')
    assert 'html' in profile.get_attribute(profile.EMAIL_EDITOR_DROPDOWN,'value'), 'Email editor selection failed'

@pytest.mark.profilepage
@pytest.mark.sanity1
def test_revert_user_preferences_footer(go_to_login_with_profile:ProfilePage):
    profile = go_to_login_with_profile
    profile.footer_user_reference_button_click()
    profile.page.wait_for_load_state('networkidle')
    assert profile.is_visible(profile.SUCCESS_MSG), 'Revert user preferences operation failed'

@pytest.mark.profilepage
@pytest.mark.sanity1
def test_revert_user_preferences_header(go_to_login_with_profile:ProfilePage):
    profile = go_to_login_with_profile
    profile.header_user_reference_button_click()
    profile.page.wait_for_load_state('networkidle')
    assert profile.is_visible(profile.SUCCESS_MSG), 'Revert user preferences operation failed'

@pytest.mark.profilepage
@pytest.mark.sanity1
def test_reset_homepage_footer(go_to_login_with_profile:ProfilePage):
    profile = go_to_login_with_profile
    profile.footer_reset_homepage_button_click()
    profile.page.wait_for_load_state('networkidle')
    assert profile.is_visible(profile.SUCCESS_MSG), 'Reset homepage operation failed'

@pytest.mark.profilepage
@pytest.mark.sanity1
def test_reset_homepage_header(go_to_login_with_profile:ProfilePage):
    profile = go_to_login_with_profile
    profile.header_reset_homepage_button_click()
    profile.page.wait_for_load_state('networkidle')
    assert profile.is_visible(profile.SUCCESS_MSG), 'Reset homepage operation failed'                       
    
    
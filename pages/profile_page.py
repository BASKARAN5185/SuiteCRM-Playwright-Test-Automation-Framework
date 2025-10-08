from pages.base_class import BaseClass

class profile_page(BaseClass):
    '''Profile Page Locators'''
    ''' User Profile under locators'''
    USER_PROFILE_HEADER="(//div[@class='col-xs-10 col-sm-11 col-md-11'])[1]"
    USER_NAME="//div[contains(text(), 'will')]"
    USER_TYPE="(//div[@type='enum'])[1]"
    PHOTO_UPLOAD=" #photo_new > input#photo_file"
    FIRST_NAME="input[name='first_name']"
    LAST_NAME="div[field='last_name'] >input[name='last_name']"
    
    '''Employee Information under locators'''
    EMPLOYEE_STATUS="(//div[contains(text() , 'Active')])[2]"
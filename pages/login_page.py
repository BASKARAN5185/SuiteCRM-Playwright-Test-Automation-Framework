from base_class import BaseClass

class LoginPage(BaseClass):
    USER_NAME='#user_name'
    USER_PASSWORD='#username_password'
    LOGIN='#bigbutton'
    HEADER_LOGO='//a[title="SuiteCRM"]'
    COMPANY_LOGO='.companylogo'
    HOME_TEXT="//*[.,text()='Welcome to the SuiteCRM 7 Demo']"

    def enter_username(self,username:str):
        self.type_text(self.USER_NAME,username)
    
    def enter_password(self, password:str):
        self.type_text(self.USER_PASSWORD,password) 
        
    def click_login_button(self):
        self.click(self.LOGIN) 
    
    def login(self,username:str,password:str) -> bool:
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
        return self.is_home_page_text_visible()
    
    def header_logo_is_visible(self) -> bool:
        return self.is_visible(self.HEADER_LOGO)
    
    def company_logo_is_visible(self) -> bool:
        return self.is_visible(self.COMPANY_LOGO)    
    
    def is_home_page_text_visible(self) -> bool:
        self.wait_for_selector(self.HOME_TEXT)        
        return self.is_visible(self.HOME_TEXT)      
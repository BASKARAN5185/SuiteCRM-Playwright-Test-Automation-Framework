from pages.base_class import BaseClass

class HomePage(BaseClass):
      HOME_ICON='a.navbar-brand with-home-icon suitepicon suitepicon-action-home'
      SALES='text="SALES"'
      MARKETING ='text="MARKETING"'
      SUPPORT='text="SUPPORT"'
      ACTIVITIES='text="ACTIVITIES"'
      COLLABORATION='text="COLLABRATION"'
      ALL='text="ALL"'
      HOME='text="HOME"'
      CREATE='text="Create"'
      SEARCH_BUTTON='button#searchbutton'
      SEARCH_TEXTBOX='input#query_string'
      NOTIFICATION_ICON='li#desktop_notifications'
      USER_ICON='button#usermenucollapsed'

      def user_icon_visible(self) -> bool:
            return self.is_visible(self.USER_ICON)
      
      def user_icon_click(self):
            self.click(self.USER_ICON)

      def notification_icon_visible(self) -> bool:
            return self.is_visible(self.NOTIFICATION_ICON)

      def notification_icon_click(self):
            self.click(self.NOTIFICATION_ICON)

      def search_button_visible(self) -> bool:
          return self.is_visible(self.SEARCH_BUTTON)
      
      def search_button_click(self):
          self.click(self.SEARCH_BUTTON)
      
      def seaerch_textbox_visible(self) -> bool:
          return self.is_visible(self.SEARCH_TEXTBOX) 

      def search_textbox_fill(self,text):
          self.fill(self.SEARCH_TEXTBOX,text)
      
      def create_click(self):
            self.click(self.CREATE)
      
      def home_icon_click(self):
          self.click(self.HOME_ICON)
          
      def sales_menu_click(self):
          self.click(self.SALES)
      
      def marketing_menu_click(self):
          self.click(self.MARKETING)
      
      def support_menu_click(self):
          self.click(self.SUPPORT)
      
      def activities_menu_click(self):
          self.click(self.ACTIVITIES)     
      
      def collabration_menu_click(self):
          self.click(self.COLLABORATION)
      
      def all_menu_click(self):
          self.click(self.ALL)    
          
      def home_dropdown_click(self):      
          self.click(self.HOME)
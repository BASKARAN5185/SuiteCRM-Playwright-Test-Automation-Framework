from base_class import BaseClass

class HomePage(BaseClass):
      HOME_ICON='a.navbar-brand with-home-icon suitepicon suitepicon-action-home'
      SALES='text="SALES"'
      MARKETING ='text="MARKETING"'
      SUPPORT='text="SUPPORT"'
      ACTIVITIES='text="ACTIVITIES"'
      COLLABORATION='text="COLLABRATION"'
      ALL='text="ALL"'
      HOME='text="HOME"'
      
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
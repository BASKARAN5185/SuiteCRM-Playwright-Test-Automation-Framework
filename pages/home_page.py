from pages.base_class import BaseClass

class HomePage(BaseClass):
      HOME_ICON='a.navbar-brand with-home-icon suitepicon suitepicon-action-home'
      ALL = '#grouptab_0'
      MARKETING ='text="MARKETING"'
      SUPPORT='text="SUPPORT"'
      ACTIVITIES='text="ACTIVITIES"'
      COLLABORATION='text="COLLABRATION"'
      ALL='#grouptab_0'
      HOME='a:has-text("Home")'
      CREATE='text="Create"'
      SEARCH_BUTTON='button#searchbutton'
      SEARCH_INPUT_BOX_BUTTON="(//button[@type='submit'])[3]"
      SEARCH_TEXTBOX='input#query_string'
      NOTIFICATION_ICON='li#desktop_notifications'
      USER_ICON = 'button#usermenucollapsed >> nth=0'


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

      def search_input_box_click(self):
          self.click(self.SEARCH_INPUT_BOX_BUTTON)

      def create_click(self):
            self.click(self.CREATE)
      
      def home_icon_click(self):
          self.click(self.HOME_ICON)
          
      def sales_menu_over(self):
          self.hover(self.SALES)
      
      def marketing_menu_over(self):
          self.hover(self.MARKETING)
      
      def support_menu_over(self):
          self.hover(self.SUPPORT)
      
      def activities_menu_over(self):   
          self.hover(self.ACTIVITIES)    
      
      def collabration_menu_over(self):
          self.hover(self.COLLABORATION)
      
      def all_menu_over(self):
         print(f"Debug: Using locator -> {self.ALL}")

         # Print the current URL and page title to confirm navigation
         print(f"Debug: Current page URL: {self.page.url}")
         print(f"Debug: Page title: {self.page.title()}")

         # Check if element exists on the page
         element = self.page.query_selector(self.ALL)
         if element:
            print(f"Debug: Element found for locator '{self.ALL}'")
         else:
            print(f"Debug: Element NOT found for locator '{self.ALL}'")

          # Try waiting for element to be visible
         try:
           self.page.wait_for_selector(self.ALL, state='visible', timeout=10000)
           print(f"Debug: Element '{self.ALL}' is visible")
         except Exception as e:
            print(f"Debug: Timeout or error waiting for element '{self.ALL}': {e}")

         # Attempt hover
         try:
           self.page.hover(self.ALL)
           print(f"Debug: Hovered over element '{self.ALL}' successfully")
         except Exception as e:
           print(f"Debug: Hover failed on element '{self.ALL}': {e}")


      def home_dropdown_click(self):      
          self.click(self.HOME)
from pages.base_class import BaseClass

class HomePage(BaseClass):
      HOME_ICON="//a[contains(@class,'navbar-brand with-home-icon')]"
      SALES = '#grouptab_0'
      MARKETING ='#grouptab_1'
      SUPPORT='#grouptab_2'
      ACTIVITIES='#grouptab_3'
      COLLABORATION='a#grouptab_4'
      ALL='#grouptab_5' 
      CREATE="(//a[@class='dropdown-toggle'])[2]"
      SEARCH_BUTTON="(//button[@id='searchbutton'])[2]"
      SEARCH_INPUT_BOX_BUTTON="(//button[@type='submit'])[3]"
      SEARCH_TEXTBOX="(//input[@id='query_string'])[3]"
      NOTIFICATION_ICON="(//button[contains(@class,'alertsButton btn')])[2]"
      USER_ICON = "(//span[@class='suitepicon suitepicon-action-current-user'])[1]"


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


      def home_dropdown_click(self,dropdown_index :int) :      
          self.click(f"(//a[@id='moduleTab_6_Home'])[{dropdown_index}]")
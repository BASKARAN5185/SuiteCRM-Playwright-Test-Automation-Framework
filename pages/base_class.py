from playwright.sync_api import sync_playwright, Page
class BaseClass:
  
  def __init__(self,page:Page):
      self.page=page
      
  def navigate_to(self, url:str):
      self.page.goto(url)   
   
  def get_page_title(self):
      return self.page.title()   
  
  def type_text(self, selector : str, text:str , Clear:bool=True):
      locator=self.page.locator(selector)
      if Clear:
          locator.fill("")
      locator.type(text) 
  
  def is_visible(self,selector:str) -> bool:     
        return  self.page.locator(selector).is_visible()
    
  def wait_for_selector(self,selector:str):
      self.page.wait_for_selector(selector)  
   
  def click(self,selector:str)-> bool:
       self.page.click(selector)    
    
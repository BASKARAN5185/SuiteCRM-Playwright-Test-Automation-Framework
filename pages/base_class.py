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
    
  def fill(self,selector:str,text:str):
       self.page.fill(selector,text)

  def get_value(self,selector:str)-> str:
        return self.page.input_value(selector)      
  
  def get_url(self)-> str:
        return self.page.url
  
  def go_back(self):
        self.page.go_back()

  def go_forward(self):
        self.page.go_forward()
  
  def  refresh_page(self):
        self.page.reload()      

  def get_text(self,selector:str)-> str:
        return self.page.text_content(selector)

  def get_attribute(self,selector:str,attribute:str)-> str:
        return self.page.get_attribute(selector,attribute)
  
  def hover(self,selector:str):
        self.page.hover(selector)
  
  def double_click(self,selector:str):
        self.page.dblclick(selector)         

  def right_click(self,selector:str):
        self.page.click(selector,button="right")
  
  def drag_and_drop(self,source_selector:str,target_selector:str):
        self.page.drag_and_drop(source_selector,target_selector)       

  def select_option_by_value(self,selector:str,value:str):
        self.page.select_option(selector,value=value)

  def select_option_by_label(self,selector:str,label:str):
        self.page.select_option(selector,label=label)     

  def select_option_by_index(self,selector:str,index:int):
        self.page.select_option(selector,index=index)     

  def check_checkbox(self,selector:str):
        self.page.check(selector)

  def uncheck_checkbox(self,selector:str):
        self.page.uncheck(selector)     
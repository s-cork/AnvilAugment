from ._anvil_designer import Form1Template
from anvil import *

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    from .. import augment
    augment.add_event(self.button_1, 'mouseenter')
    augment.add_event(self.button_1, 'focus')
    augment.add_event(self.text_box_1, 'select')
    
    augment.set_event_handler(self.text_area_1, 'keydown', self.text_area_1_keydown)
    
    self.button_1.set_event_handler('mouseenter', self.button_1_focus)
    self.button_1.set_event_handler('focus', self.button_1_focus)
    
  def button_1_focus(self, **event_args):
    print(event_args)

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.button_1.trigger('focus')

  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.text_box_1.trigger('select')
    self.text_area_1.trigger('keydown', keyCode=13)


  def text_area_1_keydown(self, **event_args):
    print(event_args)
    if event_args['key_code'] == 13:
      print(event_args['key_code'])
      return True
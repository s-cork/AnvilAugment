from ._anvil_designer import Form1Template
from anvil import *

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    from ..Augment import augment
    augment(self.button_1, 'mouseenter')
    augment(self.button_1, 'focus')
    
    self.button_1.set_event_handler('mouseenter', self.button_1_focus)
    self.button_1.set_event_handler('focus', self.button_1_focus)
    
  def button_1_focus(self, **event_args):
    print(event_args)
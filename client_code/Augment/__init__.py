from anvil import js as _js

def augment(component, event):
  if isiterable(component):
    
  _js.call_js('augment', component, event)
  
  
def isiterable(foo):
  try:
    iter(foo)
    return True
  except:
    return False




# def augment(self, event, *funcs):
#   """agument takes an event as a string - hover, focus, blur, focusin, focusout
#   if hover is the event should have two functions one for hover, and one for hover_out
#   all other events take 1 function
#   """
#   if event == 'hover':
#     func_in, func_out = funcs
#     func_in = func_in.im_func.__name__
#     func_out = func_out.im_func.__name__
#     js.call_js('augment_hover', self, func_in, func_out)
#   else:  
#     func = funcs[0]
#     func = func.im_func.__name__
#     js.call_js('augment', self, event, func)


# def augment_trigger(self, event):
#   """expects and event like click or focus or select"""
#   js.call_js('augment_trigger', self, event)


# components = [Button, Link, Label, TextBox, TextArea, Image, ColumnPanel]


# for c in components:
#   c.augment = augment
#   c.augment_trigger = augment_trigger


  
  
from anvil import js as _js

def add_event(component, event):
  if not isinstance(event, str):
    raise TypeError(f'event must be type str and not {type(event)}')
  _js.call_js('augment', component, event)
  
  
def set_event_handler(component, event, func):
  add_event(component, event)
  component.set_event_handler(event, func)
  
if __name__ == '__main__':
  print('this is a dependency')
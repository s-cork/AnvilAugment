from anvil import js as _js

def add_event(component, event, **event_args):
  print(event_args)
  if not isinstance(event, str):
    raise TypeError(f'event must be type str and not {type(event)}')
  if not event_args:
    event_args = None
  _js.call_js('augment', component, event, event_args)
  
  
def set_event_handler(component, event, func, **event_args):
  add_event(component, event, **event_args)
  component.set_event_handler(event, func)
  
if __name__ == '__main__':
  print('this is a dependency')
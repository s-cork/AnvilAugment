from anvil import js as _js

def augment(component, event):
  if not isinstance(event, str):
    raise TypeError(f'event must be type str and not {type(event)}')
  _js.call_js('augment', component, event)
  
  
if __name__ == '__main__':
  print('this is a dependency')
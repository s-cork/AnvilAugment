"""
    AnvilAugment
    Copyright 2020 Stu Cork

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Source code published at https://github.com/s-cork/AnvilAugment
"""

from anvil import js as _js, Component as _Component
import anvil as _anvil
from anvil.js.window import jQuery as _S

def add_event(component, event):
  """component: (instantiated) anvil component
  event: str - any jquery event string
  """
  init(component) # adds the trigger method to the component type
  if not isinstance(event, str):
      raise TypeError('event must be type str and not ' + type(event))
  
  _js.call_js('add_event', component, event)
  
  js_event_name = 'mouseenter mouseleave' if event is 'hover' else event
  if 'key' not in event:
      def standard_handler(e):
          if component.raise_event(event, sender=component, event_type=e.type):
              e.preventDefault()

      handler = standard_handler

  else:
      def key_handler(e):
          if component.raise_event( event, 
                                    sender=component, 
                                    event_type=e.type, 
                                    key=e.key,
                                    key_code=e.keyCode,
                                    shift_key=e.shiftKey,
                                    alt_key=e.altKey,
                                    meta_key=e.metaKey,
                                    ctrl_key=e.ctrlKey,
                                   ):
              e.preventDefault()
      
      handler = key_handler


  _S(_get_node_for_component(component)).on(js_event_name, handler)
  
  
def set_event_handler(component, event, func):
  """component: (instantiated) anvil compoent
  event: str - any jquery event string
  func: function to handle the event
  """
  add_event(component, event)
  component.set_event_handler(event, func)


def init(component):
  """adds a trigger method to all components of the type passed in"""
  if isinstance(component, _Component):
    component = type(component)
  if issubclass(component, _Component):
    pass
  else:
    raise TypeError("expected a component not {}".format(type(component).__name__))
  if hasattr(component, 'trigger'):
    return
  else:
    component.trigger = trigger


def trigger(self, event):
    """trigger an event self is an anvil component, event is a component, event is a str or a dictionary
    if event is a dictionary it should include an event key e.g. {'event': 'keypress', 'which': 13}
    """
    if isinstance(event, dict):
        event_name = event.get('event')
        event = _S.Event(event_name, event)
    event = 'mouseenter mouseleave' if event is 'hover' else event
    _S(_get_node_for_component(self)).trigger(event)


def _get_node_for_component(component):
    if isinstance(component, _anvil.Button):
        return _js.get_dom_node(component).firstElementChild
    elif isinstance(component, _anvil.FileLoader):
        return _S(_js.get_dom_node(component)).find('form')
    else:
        return _js.get_dom_node(component)
  
  
if __name__ == '__main__':
  _ = _anvil.Label()
  _.set_event_handler('show', lambda **e: _anvil.Notification('oops hashrouting is a dependency', timeout=None).show())
  _anvil.open_form(_)

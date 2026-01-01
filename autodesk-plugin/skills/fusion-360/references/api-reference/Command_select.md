# Command.select Event

Parent Object: [Command](Command.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/Command.h>

## Description

This even fires when the user selects an entity. This is different from the preselect where an entity is shown as being available for selection as the mouse passes over the entity. This is the actual selection where the user has clicked the mouse on the entity.

## Syntax

* [Python Using fusion360utils](#PythonUsingFusion360Utils)
* [Python](#Python)
* [C++](#C++)

*-------- Import ---------* ```` ``` # Import fusion360utils folder, which includes event_utils.py. from ...lib import fusion360utils as futil ``` ```` *-------- Global variables ---------* ```` ``` # Global variable used to maintain a reference to all event handlers. local_handlers = [] ``` ```` *-------- Connect the handler to the event. ---------* ```` ``` # "command_var" is a variable referencing a Command object. # "command_select" is the event handler function. futil.add_handler(command_var.select, command_select, local_handlers=local_handlers) ``` ```` *-------- Event handler function definition ---------* ```` ``` # Event handler for the select event. def command_select(args: adsk.core.SelectionEventArgs):     # Code to react to the event.     app.log('In command_select event handler.') ``` ```` |

*-------- Global variables ---------* ```` ``` # Global variable used to maintain a reference to all event handlers. handlers = [] ``` ```` *-------- Connect the handler to the event. ---------* ```` ``` # "command_var" is a variable referencing a Command object. # "MySelectHandler" is the name of the class that handles the event. onSelect = MySelectHandler() command_var.select.add(onSelect) handlers.append(onSelect) ``` ```` *-------- Event handler class definition ---------* ```` ``` # Event handler for the select event. class MySelectHandler(adsk.core.SelectionEventHandler):     def __init__(self):         super().__init__()     def notify(self, args: adsk.core.SelectionEventArgs):         # Code to react to the event.         app.log('In MySelectHandler event handler.') ``` ```` |

*--------- Required include files. ---------* ```` ``` #include <Core/UserInterface/Command.h> #include <Core/UserInterface/SelectionEvent.h> #include <Core/UserInterface/SelectionEventHandler.h> #include <Core/UserInterface/SelectionEventArgs.h> ``` ````  *--------- Event handler class definition and global declaration. --------- ```` ``` // Event handler for the select event. ``` ````* class MySelectEventHandler : public adsk::core::SelectionEventHandler { public:  void notify(const Ptr<SelectionEventArgs>& eventArgs) override  {  // Code to react to the event.  ui->messageBox("In MySelectEventHandler event handler.");  } } \_select;  *--------- Connect the handler to the event. ---------* ```` ``` // "command_var" is a variable referencing a Command object. // Connect the handler function to the event. Ptr<SelectionEvent> selectEvent = command_var->select(); if (!selectEvent)     return;  bool isOk = selectEvent->add(&_select); if (!isOk)     return; ``` ```` |

## Property Value

This is an event property that returns a [SelectionEvent](SelectionEvent.htm).

## Version

Introduced in version April 2019

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
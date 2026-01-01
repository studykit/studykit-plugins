# Command.unselect Event

Parent Object: [Command](Command.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/Command.h>

## Description

This even fires when the user unselects an entity by clicking the mouse again on selected entity or canceling previous selection.

## Syntax

* [Python Using fusion360utils](#PythonUsingFusion360Utils)
* [Python](#Python)
* [C++](#C++)

*-------- Import ---------* ```` ``` # Import fusion360utils folder, which includes event_utils.py. from ...lib import fusion360utils as futil ``` ```` *-------- Global variables ---------* ```` ``` # Global variable used to maintain a reference to all event handlers. local_handlers = [] ``` ```` *-------- Connect the handler to the event. ---------* ```` ``` # "command_var" is a variable referencing a Command object. # "command_unselect" is the event handler function. futil.add_handler(command_var.unselect, command_unselect, local_handlers=local_handlers) ``` ```` *-------- Event handler function definition ---------* ```` ``` # Event handler for the unselect event. def command_unselect(args: adsk.core.SelectionEventArgs):     # Code to react to the event.     app.log('In command_unselect event handler.') ``` ```` |

*-------- Global variables ---------* ```` ``` # Global variable used to maintain a reference to all event handlers. handlers = [] ``` ```` *-------- Connect the handler to the event. ---------* ```` ``` # "command_var" is a variable referencing a Command object. # "MyUnselectHandler" is the name of the class that handles the event. onUnselect = MyUnselectHandler() command_var.unselect.add(onUnselect) handlers.append(onUnselect) ``` ```` *-------- Event handler class definition ---------* ```` ``` # Event handler for the unselect event. class MyUnselectHandler(adsk.core.SelectionEventHandler):     def __init__(self):         super().__init__()     def notify(self, args: adsk.core.SelectionEventArgs):         # Code to react to the event.         app.log('In MyUnselectHandler event handler.') ``` ```` |

*--------- Required include files. ---------* ```` ``` #include <Core/UserInterface/Command.h> #include <Core/UserInterface/SelectionEvent.h> #include <Core/UserInterface/SelectionEventHandler.h> #include <Core/UserInterface/SelectionEventArgs.h> ``` ````  *--------- Event handler class definition and global declaration. --------- ```` ``` // Event handler for the unselect event. ``` ````* class MyUnselectEventHandler : public adsk::core::SelectionEventHandler { public:  void notify(const Ptr<SelectionEventArgs>& eventArgs) override  {  // Code to react to the event.  ui->messageBox("In MyUnselectEventHandler event handler.");  } } \_unselect;  *--------- Connect the handler to the event. ---------* ```` ``` // "command_var" is a variable referencing a Command object. // Connect the handler function to the event. Ptr<SelectionEvent> unselectEvent = command_var->unselect(); if (!unselectEvent)     return;  bool isOk = unselectEvent->add(&_unselect); if (!isOk)     return; ``` ```` |

## Property Value

This is an event property that returns a [SelectionEvent](SelectionEvent.htm).

## Version

Introduced in version April 2019

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
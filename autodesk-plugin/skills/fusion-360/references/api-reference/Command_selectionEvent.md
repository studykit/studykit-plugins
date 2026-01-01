# Command.selectionEvent Event

Parent Object: [Command](Command.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/Command.h>

## Description

This function is retired. See more information in the 'Remarks' section below.

## Remarks

This event has been retired. Equivalent functionality is provide by the preSelect event.

## Syntax

* [Python Using fusion360utils](#PythonUsingFusion360Utils)
* [Python](#Python)
* [C++](#C++)

*-------- Import ---------* ```` ``` # Import fusion360utils folder, which includes event_utils.py. from ...lib import fusion360utils as futil ``` ```` *-------- Global variables ---------* ```` ``` # Global variable used to maintain a reference to all event handlers. local_handlers = [] ``` ```` *-------- Connect the handler to the event. ---------* ```` ``` # "command_var" is a variable referencing a Command object. # "command_selectionEvent" is the event handler function. futil.add_handler(command_var.selectionEvent, command_selectionEvent, local_handlers=local_handlers) ``` ```` *-------- Event handler function definition ---------* ```` ``` # Event handler for the selectionEvent event. def command_selectionEvent(args: adsk.core.SelectionEventArgs):     # Code to react to the event.     app.log('In command_selectionEvent event handler.') ``` ```` |

*-------- Global variables ---------* ```` ``` # Global variable used to maintain a reference to all event handlers. handlers = [] ``` ```` *-------- Connect the handler to the event. ---------* ```` ``` # "command_var" is a variable referencing a Command object. # "MySelectionEventHandler" is the name of the class that handles the event. onSelectionEvent = MySelectionEventHandler() command_var.selectionEvent.add(onSelectionEvent) handlers.append(onSelectionEvent) ``` ```` *-------- Event handler class definition ---------* ```` ``` # Event handler for the selectionEvent event. class MySelectionEventHandler(adsk.core.SelectionEventHandler):     def __init__(self):         super().__init__()     def notify(self, args: adsk.core.SelectionEventArgs):         # Code to react to the event.         app.log('In MySelectionEventHandler event handler.') ``` ```` |

*--------- Required include files. ---------* ```` ``` #include <Core/UserInterface/Command.h> #include <Core/UserInterface/SelectionEvent.h> #include <Core/UserInterface/SelectionEventHandler.h> #include <Core/UserInterface/SelectionEventArgs.h> ``` ````  *--------- Event handler class definition and global declaration. --------- ```` ``` // Event handler for the selectionEvent event. ``` ````* class MySelectionEventEventHandler : public adsk::core::SelectionEventHandler { public:  void notify(const Ptr<SelectionEventArgs>& eventArgs) override  {  // Code to react to the event.  ui->messageBox("In MySelectionEventEventHandler event handler.");  } } \_selectionEvent;  *--------- Connect the handler to the event. ---------* ```` ``` // "command_var" is a variable referencing a Command object. // Connect the handler function to the event. Ptr<SelectionEvent> selectionEventEvent = command_var->selectionEvent(); if (!selectionEventEvent)     return;  bool isOk = selectionEventEvent->add(&_selectionEvent); if (!isOk)     return; ``` ```` |

## Property Value

This is an event property that returns a [SelectionEvent](SelectionEvent.htm).

## Version

Introduced in version June 2015
Retired in version July 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
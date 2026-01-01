# Command.preSelectMouseMove Event

Parent Object: [Command](Command.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/Command.h>

## Description

This event fires continually while the mouse is moved over an entity that is valid for selected.

## Syntax

* [Python Using fusion360utils](#PythonUsingFusion360Utils)
* [Python](#Python)
* [C++](#C++)

*-------- Import ---------* ```` ``` # Import fusion360utils folder, which includes event_utils.py. from ...lib import fusion360utils as futil ``` ```` *-------- Global variables ---------* ```` ``` # Global variable used to maintain a reference to all event handlers. local_handlers = [] ``` ```` *-------- Connect the handler to the event. ---------* ```` ``` # "command_var" is a variable referencing a Command object. # "command_preSelectMouseMove" is the event handler function. futil.add_handler(command_var.preSelectMouseMove, command_preSelectMouseMove, local_handlers=local_handlers) ``` ```` *-------- Event handler function definition ---------* ```` ``` # Event handler for the preSelectMouseMove event. def command_preSelectMouseMove(args: adsk.core.SelectionEventArgs):     # Code to react to the event.     app.log('In command_preSelectMouseMove event handler.') ``` ```` |

*-------- Global variables ---------* ```` ``` # Global variable used to maintain a reference to all event handlers. handlers = [] ``` ```` *-------- Connect the handler to the event. ---------* ```` ``` # "command_var" is a variable referencing a Command object. # "MyPreSelectMouseMoveHandler" is the name of the class that handles the event. onPreSelectMouseMove = MyPreSelectMouseMoveHandler() command_var.preSelectMouseMove.add(onPreSelectMouseMove) handlers.append(onPreSelectMouseMove) ``` ```` *-------- Event handler class definition ---------* ```` ``` # Event handler for the preSelectMouseMove event. class MyPreSelectMouseMoveHandler(adsk.core.SelectionEventHandler):     def __init__(self):         super().__init__()     def notify(self, args: adsk.core.SelectionEventArgs):         # Code to react to the event.         app.log('In MyPreSelectMouseMoveHandler event handler.') ``` ```` |

*--------- Required include files. ---------* ```` ``` #include <Core/UserInterface/Command.h> #include <Core/UserInterface/SelectionEvent.h> #include <Core/UserInterface/SelectionEventHandler.h> #include <Core/UserInterface/SelectionEventArgs.h> ``` ````  *--------- Event handler class definition and global declaration. --------- ```` ``` // Event handler for the preSelectMouseMove event. ``` ````* class MyPreSelectMouseMoveEventHandler : public adsk::core::SelectionEventHandler { public:  void notify(const Ptr<SelectionEventArgs>& eventArgs) override  {  // Code to react to the event.  ui->messageBox("In MyPreSelectMouseMoveEventHandler event handler.");  } } \_preSelectMouseMove;  *--------- Connect the handler to the event. ---------* ```` ``` // "command_var" is a variable referencing a Command object. // Connect the handler function to the event. Ptr<SelectionEvent> preSelectMouseMoveEvent = command_var->preSelectMouseMove(); if (!preSelectMouseMoveEvent)     return;  bool isOk = preSelectMouseMoveEvent->add(&_preSelectMouseMove); if (!isOk)     return; ``` ```` |

## Property Value

This is an event property that returns a [SelectionEvent](SelectionEvent.htm).

## Version

Introduced in version April 2019

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
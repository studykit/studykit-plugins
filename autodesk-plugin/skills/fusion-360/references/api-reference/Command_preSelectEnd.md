# Command.preSelectEnd Event

Parent Object: [Command](Command.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/Command.h>

## Description

This event fires when the moused is moved away from an entity that was in a pre-select state. If your add-in has done something in reaction to the preSelect event, like draw some custom graphics, this event provides the notification to clean up whatever you've done that's associated with the current pre-select.

## Syntax

* [Python Using fusion360utils](#PythonUsingFusion360Utils)
* [Python](#Python)
* [C++](#C++)

*-------- Import ---------* ```` ``` # Import fusion360utils folder, which includes event_utils.py. from ...lib import fusion360utils as futil ``` ```` *-------- Global variables ---------* ```` ``` # Global variable used to maintain a reference to all event handlers. local_handlers = [] ``` ```` *-------- Connect the handler to the event. ---------* ```` ``` # "command_var" is a variable referencing a Command object. # "command_preSelectEnd" is the event handler function. futil.add_handler(command_var.preSelectEnd, command_preSelectEnd, local_handlers=local_handlers) ``` ```` *-------- Event handler function definition ---------* ```` ``` # Event handler for the preSelectEnd event. def command_preSelectEnd(args: adsk.core.SelectionEventArgs):     # Code to react to the event.     app.log('In command_preSelectEnd event handler.') ``` ```` |

*-------- Global variables ---------* ```` ``` # Global variable used to maintain a reference to all event handlers. handlers = [] ``` ```` *-------- Connect the handler to the event. ---------* ```` ``` # "command_var" is a variable referencing a Command object. # "MyPreSelectEndHandler" is the name of the class that handles the event. onPreSelectEnd = MyPreSelectEndHandler() command_var.preSelectEnd.add(onPreSelectEnd) handlers.append(onPreSelectEnd) ``` ```` *-------- Event handler class definition ---------* ```` ``` # Event handler for the preSelectEnd event. class MyPreSelectEndHandler(adsk.core.SelectionEventHandler):     def __init__(self):         super().__init__()     def notify(self, args: adsk.core.SelectionEventArgs):         # Code to react to the event.         app.log('In MyPreSelectEndHandler event handler.') ``` ```` |

*--------- Required include files. ---------* ```` ``` #include <Core/UserInterface/Command.h> #include <Core/UserInterface/SelectionEvent.h> #include <Core/UserInterface/SelectionEventHandler.h> #include <Core/UserInterface/SelectionEventArgs.h> ``` ````  *--------- Event handler class definition and global declaration. --------- ```` ``` // Event handler for the preSelectEnd event. ``` ````* class MyPreSelectEndEventHandler : public adsk::core::SelectionEventHandler { public:  void notify(const Ptr<SelectionEventArgs>& eventArgs) override  {  // Code to react to the event.  ui->messageBox("In MyPreSelectEndEventHandler event handler.");  } } \_preSelectEnd;  *--------- Connect the handler to the event. ---------* ```` ``` // "command_var" is a variable referencing a Command object. // Connect the handler function to the event. Ptr<SelectionEvent> preSelectEndEvent = command_var->preSelectEnd(); if (!preSelectEndEvent)     return;  bool isOk = preSelectEndEvent->add(&_preSelectEnd); if (!isOk)     return; ``` ```` |

## Property Value

This is an event property that returns a [SelectionEvent](SelectionEvent.htm).

## Version

Introduced in version April 2019

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
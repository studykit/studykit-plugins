# Command.preSelectStart Event

Parent Object: [Command](Command.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/Command.h>

## Description

As the mouse moves over entities in the graphics window, entities valid for selection are highlighted. Before an entity is highlighted, Fusion determines if it is a valid selectable entity using the selection filter defined on the SelectionCommandInput and the preSelect event of the command. The preSelectStart event fires when the mouse first moves over an entity valid for selection. You can obtain the entity and mouse position from the Selection object returned by the selection property of the SelectionEventArgs object provided through the event.

## Syntax

* [Python Using fusion360utils](#PythonUsingFusion360Utils)
* [Python](#Python)
* [C++](#C++)

*-------- Import ---------* ```` ``` # Import fusion360utils folder, which includes event_utils.py. from ...lib import fusion360utils as futil ``` ```` *-------- Global variables ---------* ```` ``` # Global variable used to maintain a reference to all event handlers. local_handlers = [] ``` ```` *-------- Connect the handler to the event. ---------* ```` ``` # "command_var" is a variable referencing a Command object. # "command_preSelectStart" is the event handler function. futil.add_handler(command_var.preSelectStart, command_preSelectStart, local_handlers=local_handlers) ``` ```` *-------- Event handler function definition ---------* ```` ``` # Event handler for the preSelectStart event. def command_preSelectStart(args: adsk.core.SelectionEventArgs):     # Code to react to the event.     app.log('In command_preSelectStart event handler.') ``` ```` |

*-------- Global variables ---------* ```` ``` # Global variable used to maintain a reference to all event handlers. handlers = [] ``` ```` *-------- Connect the handler to the event. ---------* ```` ``` # "command_var" is a variable referencing a Command object. # "MyPreSelectStartHandler" is the name of the class that handles the event. onPreSelectStart = MyPreSelectStartHandler() command_var.preSelectStart.add(onPreSelectStart) handlers.append(onPreSelectStart) ``` ```` *-------- Event handler class definition ---------* ```` ``` # Event handler for the preSelectStart event. class MyPreSelectStartHandler(adsk.core.SelectionEventHandler):     def __init__(self):         super().__init__()     def notify(self, args: adsk.core.SelectionEventArgs):         # Code to react to the event.         app.log('In MyPreSelectStartHandler event handler.') ``` ```` |

*--------- Required include files. ---------* ```` ``` #include <Core/UserInterface/Command.h> #include <Core/UserInterface/SelectionEvent.h> #include <Core/UserInterface/SelectionEventHandler.h> #include <Core/UserInterface/SelectionEventArgs.h> ``` ````  *--------- Event handler class definition and global declaration. --------- ```` ``` // Event handler for the preSelectStart event. ``` ````* class MyPreSelectStartEventHandler : public adsk::core::SelectionEventHandler { public:  void notify(const Ptr<SelectionEventArgs>& eventArgs) override  {  // Code to react to the event.  ui->messageBox("In MyPreSelectStartEventHandler event handler.");  } } \_preSelectStart;  *--------- Connect the handler to the event. ---------* ```` ``` // "command_var" is a variable referencing a Command object. // Connect the handler function to the event. Ptr<SelectionEvent> preSelectStartEvent = command_var->preSelectStart(); if (!preSelectStartEvent)     return;  bool isOk = preSelectStartEvent->add(&_preSelectStart); if (!isOk)     return; ``` ```` |

## Property Value

This is an event property that returns a [SelectionEvent](SelectionEvent.htm).

## Version

Introduced in version May 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
# Command.activate Event

Parent Object: [Command](Command.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/Command.h>

## Description

Gets an event that is fired when the command is first activated or re-activated after being suspended.

## Syntax

* [Python Using fusion360utils](#PythonUsingFusion360Utils)
* [Python](#Python)
* [C++](#C++)

*-------- Import ---------* |

*-------- Global variables ---------* ```` ``` # Global variable used to maintain a reference to all event handlers. handlers = [] ``` ```` *-------- Connect the handler to the event. ---------* ```` ``` # "command_var" is a variable referencing a Command object. # "MyActivateHandler" is the name of the class that handles the event. onActivate = MyActivateHandler() command_var.activate.add(onActivate) handlers.append(onActivate) ``` ```` *-------- Event handler class definition ---------* ```` ``` # Event handler for the activate event. class MyActivateHandler(adsk.core.CommandEventHandler):     def __init__(self):         super().__init__()     def notify(self, args: adsk.core.CommandEventArgs):         # Code to react to the event.         app.log('In MyActivateHandler event handler.') ``` ```` |

*--------- Required include files. ---------* ```` ``` #include <Core/UserInterface/Command.h> #include <Core/UserInterface/CommandEvent.h> #include <Core/UserInterface/CommandEventHandler.h> #include <Core/UserInterface/CommandEventArgs.h> ``` ````  *--------- Event handler class definition and global declaration. --------- ```` ``` // Event handler for the activate event. ``` ````* class MyActivateEventHandler : public adsk::core::CommandEventHandler { public:  void notify(const Ptr<CommandEventArgs>& eventArgs) override  {  // Code to react to the event.  ui->messageBox("In MyActivateEventHandler event handler.");  } } \_activate;  *--------- Connect the handler to the event. ---------* ```` ``` // "command_var" is a variable referencing a Command object. // Connect the handler function to the event. Ptr<CommandEvent> activateEvent = command_var->activate(); if (!activateEvent)     return;  bool isOk = activateEvent->add(&_activate); if (!isOk)     return; ``` ```` |

## Property Value

This is an event property that returns a [CommandEvent](CommandEvent.htm).

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [CommandEvent](CommandEvent.htm) | Returns a CommandEvent object that is used to connect and release from the event. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
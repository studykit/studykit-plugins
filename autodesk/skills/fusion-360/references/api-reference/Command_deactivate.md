# Command.deactivate Event

Parent Object: [Command](Command.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/Command.h>

## Description

Gets an event that is fired when the command is deactivated. The command still exists and could still be activated again.

## Syntax

* [Python Using fusion360utils](#PythonUsingFusion360Utils)
* [Python](#Python)
* [C++](#C++)

*-------- Import ---------* |

*-------- Global variables ---------* ```` ``` # Global variable used to maintain a reference to all event handlers. handlers = [] ``` ```` *-------- Connect the handler to the event. ---------* ```` ``` # "command_var" is a variable referencing a Command object. # "MyDeactivateHandler" is the name of the class that handles the event. onDeactivate = MyDeactivateHandler() command_var.deactivate.add(onDeactivate) handlers.append(onDeactivate) ``` ```` *-------- Event handler class definition ---------* ```` ``` # Event handler for the deactivate event. class MyDeactivateHandler(adsk.core.CommandEventHandler):     def __init__(self):         super().__init__()     def notify(self, args: adsk.core.CommandEventArgs):         # Code to react to the event.         app.log('In MyDeactivateHandler event handler.') ``` ```` |

*--------- Required include files. ---------* ```` ``` #include <Core/UserInterface/Command.h> #include <Core/UserInterface/CommandEvent.h> #include <Core/UserInterface/CommandEventHandler.h> #include <Core/UserInterface/CommandEventArgs.h> ``` ````  *--------- Event handler class definition and global declaration. --------- ```` ``` // Event handler for the deactivate event. ``` ````* class MyDeactivateEventHandler : public adsk::core::CommandEventHandler { public:  void notify(const Ptr<CommandEventArgs>& eventArgs) override  {  // Code to react to the event.  ui->messageBox("In MyDeactivateEventHandler event handler.");  } } \_deactivate;  *--------- Connect the handler to the event. ---------* ```` ``` // "command_var" is a variable referencing a Command object. // Connect the handler function to the event. Ptr<CommandEvent> deactivateEvent = command_var->deactivate(); if (!deactivateEvent)     return;  bool isOk = deactivateEvent->add(&_deactivate); if (!isOk)     return; ``` ```` |

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
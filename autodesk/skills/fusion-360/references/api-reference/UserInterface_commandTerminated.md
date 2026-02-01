# UserInterface.commandTerminated Event

Parent Object: [UserInterface](UserInterface.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/UserInterface.h>

## Description

Gets an event that is fired when a command is terminated.

## Syntax

* [Python Using fusion360utils](#PythonUsingFusion360Utils)
* [Python](#Python)
* [C++](#C++)

*-------- Import ---------* |

*-------- Global variables ---------* ```` ``` # Global variable used to maintain a reference to all event handlers. handlers = [] ``` ```` *-------- Connect the handler to the event. ---------* ```` ``` # "userInterface_var" is a variable referencing a UserInterface object. # "MyCommandTerminatedHandler" is the name of the class that handles the event. onCommandTerminated = MyCommandTerminatedHandler() userInterface_var.commandTerminated.add(onCommandTerminated) handlers.append(onCommandTerminated) ``` ```` *-------- Event handler class definition ---------* ```` ``` # Event handler for the commandTerminated event. class MyCommandTerminatedHandler(adsk.core.ApplicationCommandEventHandler):     def __init__(self):         super().__init__()     def notify(self, args: adsk.core.ApplicationCommandEventArgs):         # Code to react to the event.         app.log('In MyCommandTerminatedHandler event handler.') ``` ```` |

*--------- Required include files. ---------* ```` ``` #include <Core/UserInterface/UserInterface.h> #include <Core/UserInterface/ApplicationCommandEvent.h> #include <Core/UserInterface/ApplicationCommandEventHandler.h> #include <Core/UserInterface/ApplicationCommandEventArgs.h> ``` ````  *--------- Event handler class definition and global declaration. --------- ```` ``` // Event handler for the commandTerminated event. ``` ````* class MyCommandTerminatedEventHandler : public adsk::core::ApplicationCommandEventHandler { public:  void notify(const Ptr<ApplicationCommandEventArgs>& eventArgs) override  {  // Code to react to the event.  ui->messageBox("In MyCommandTerminatedEventHandler event handler.");  } } \_commandTerminated;  *--------- Connect the handler to the event. ---------* ```` ``` // "userInterface_var" is a variable referencing a UserInterface object. // Connect the handler function to the event. Ptr<ApplicationCommandEvent> commandTerminatedEvent = userInterface_var->commandTerminated(); if (!commandTerminatedEvent)     return;  bool isOk = commandTerminatedEvent->add(&_commandTerminated); if (!isOk)     return; ``` ```` |

## Property Value

This is an event property that returns an [ApplicationCommandEvent](ApplicationCommandEvent.htm).

## Version

Introduced in version November 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
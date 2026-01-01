# UserInterface.commandCreated Event

Parent Object: [UserInterface](UserInterface.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/UserInterface.h>

## Description

The commandCreated event fires immediately after the command is created.

## Syntax

* [Python Using fusion360utils](#PythonUsingFusion360Utils)
* [Python](#Python)
* [C++](#C++)

*-------- Import ---------* |

*-------- Global variables ---------* ```` ``` # Global variable used to maintain a reference to all event handlers. handlers = [] ``` ```` *-------- Connect the handler to the event. ---------* ```` ``` # "userInterface_var" is a variable referencing a UserInterface object. # "MyCommandCreatedHandler" is the name of the class that handles the event. onCommandCreated = MyCommandCreatedHandler() userInterface_var.commandCreated.add(onCommandCreated) handlers.append(onCommandCreated) ``` ```` *-------- Event handler class definition ---------* ```` ``` # Event handler for the commandCreated event. class MyCommandCreatedHandler(adsk.core.ApplicationCommandEventHandler):     def __init__(self):         super().__init__()     def notify(self, args: adsk.core.ApplicationCommandEventArgs):         # Code to react to the event.         app.log('In MyCommandCreatedHandler event handler.') ``` ```` |

*--------- Required include files. ---------* ```` ``` #include <Core/UserInterface/UserInterface.h> #include <Core/UserInterface/ApplicationCommandEvent.h> #include <Core/UserInterface/ApplicationCommandEventHandler.h> #include <Core/UserInterface/ApplicationCommandEventArgs.h> ``` ````  *--------- Event handler class definition and global declaration. --------- ```` ``` // Event handler for the commandCreated event. ``` ````* class MyCommandCreatedEventHandler : public adsk::core::ApplicationCommandEventHandler { public:  void notify(const Ptr<ApplicationCommandEventArgs>& eventArgs) override  {  // Code to react to the event.  ui->messageBox("In MyCommandCreatedEventHandler event handler.");  } } \_commandCreated;  *--------- Connect the handler to the event. ---------* ```` ``` // "userInterface_var" is a variable referencing a UserInterface object. // Connect the handler function to the event. Ptr<ApplicationCommandEvent> commandCreatedEvent = userInterface_var->commandCreated(); if (!commandCreatedEvent)     return;  bool isOk = commandCreatedEvent->add(&_commandCreated); if (!isOk)     return; ``` ```` |

## Property Value

This is an event property that returns an [ApplicationCommandEvent](ApplicationCommandEvent.htm).

## Version

Introduced in version November 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
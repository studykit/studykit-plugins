# UserInterface.commandStarting Event

Parent Object: [UserInterface](UserInterface.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/UserInterface.h>

## Description

The commandStarting event fires when a request for a command to be executed has been received but before the command is executed. Through this event, it's possible to cancel the command from being executed.

## Syntax

* [Python Using fusion360utils](#PythonUsingFusion360Utils)
* [Python](#Python)
* [C++](#C++)

*-------- Import ---------* |

*-------- Global variables ---------* ```` ``` # Global variable used to maintain a reference to all event handlers. handlers = [] ``` ```` *-------- Connect the handler to the event. ---------* ```` ``` # "userInterface_var" is a variable referencing a UserInterface object. # "MyCommandStartingHandler" is the name of the class that handles the event. onCommandStarting = MyCommandStartingHandler() userInterface_var.commandStarting.add(onCommandStarting) handlers.append(onCommandStarting) ``` ```` *-------- Event handler class definition ---------* ```` ``` # Event handler for the commandStarting event. class MyCommandStartingHandler(adsk.core.ApplicationCommandEventHandler):     def __init__(self):         super().__init__()     def notify(self, args: adsk.core.ApplicationCommandEventArgs):         # Code to react to the event.         app.log('In MyCommandStartingHandler event handler.') ``` ```` |

*--------- Required include files. ---------* ```` ``` #include <Core/UserInterface/UserInterface.h> #include <Core/UserInterface/ApplicationCommandEvent.h> #include <Core/UserInterface/ApplicationCommandEventHandler.h> #include <Core/UserInterface/ApplicationCommandEventArgs.h> ``` ````  *--------- Event handler class definition and global declaration. --------- ```` ``` // Event handler for the commandStarting event. ``` ````* class MyCommandStartingEventHandler : public adsk::core::ApplicationCommandEventHandler { public:  void notify(const Ptr<ApplicationCommandEventArgs>& eventArgs) override  {  // Code to react to the event.  ui->messageBox("In MyCommandStartingEventHandler event handler.");  } } \_commandStarting;  *--------- Connect the handler to the event. ---------* ```` ``` // "userInterface_var" is a variable referencing a UserInterface object. // Connect the handler function to the event. Ptr<ApplicationCommandEvent> commandStartingEvent = userInterface_var->commandStarting(); if (!commandStartingEvent)     return;  bool isOk = commandStartingEvent->add(&_commandStarting); if (!isOk)     return; ``` ```` |

## Property Value

This is an event property that returns an [ApplicationCommandEvent](ApplicationCommandEvent.htm).

## Version

Introduced in version November 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
# CommandDefinition.commandCreated Event

Parent Object: [CommandDefinition](CommandDefinition.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/CommandDefinition.h>

## Description

This event is fired when the associated control is manipulated by the user. A new Command object is created and passed back through this event which you can then use to interact with the user to get any input the command requires.

## Syntax

* [Python Using fusion360utils](#PythonUsingFusion360Utils)
* [Python](#Python)
* [C++](#C++)

*-------- Import ---------* |

*-------- Global variables ---------* ```` ``` # Global variable used to maintain a reference to all event handlers. handlers = [] ``` ```` *-------- Connect the handler to the event. ---------* ```` ``` # "commandDefinition_var" is a variable referencing a CommandDefinition object. # "MyCommandCreatedHandler" is the name of the class that handles the event. onCommandCreated = MyCommandCreatedHandler() commandDefinition_var.commandCreated.add(onCommandCreated) handlers.append(onCommandCreated) ``` ```` *-------- Event handler class definition ---------* ```` ``` # Event handler for the commandCreated event. class MyCommandCreatedHandler(adsk.core.CommandCreatedEventHandler):     def __init__(self):         super().__init__()     def notify(self, args: adsk.core.CommandCreatedEventArgs):         # Code to react to the event.         app.log('In MyCommandCreatedHandler event handler.') ``` ```` |

*--------- Required include files. ---------* ```` ``` #include <Core/UserInterface/CommandDefinition.h> #include <Core/UserInterface/CommandCreatedEvent.h> #include <Core/UserInterface/CommandCreatedEventHandler.h> #include <Core/UserInterface/CommandCreatedEventArgs.h> ``` ````  *--------- Event handler class definition and global declaration. --------- ```` ``` // Event handler for the commandCreated event. ``` ````* class MyCommandCreatedEventHandler : public adsk::core::CommandCreatedEventHandler { public:  void notify(const Ptr<CommandCreatedEventArgs>& eventArgs) override  {  // Code to react to the event.  ui->messageBox("In MyCommandCreatedEventHandler event handler.");  } } \_commandCreated;  *--------- Connect the handler to the event. ---------* ```` ``` // "commandDefinition_var" is a variable referencing a CommandDefinition object. // Connect the handler function to the event. Ptr<CommandCreatedEvent> commandCreatedEvent = commandDefinition_var->commandCreated(); if (!commandCreatedEvent)     return;  bool isOk = commandCreatedEvent->add(&_commandCreated); if (!isOk)     return; ``` ```` |

## Property Value

This is an event property that returns a [CommandCreatedEvent](CommandCreatedEvent.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Command Inputs API Sample](CommandInputsSample_Sample.htm) | Creates a command dialog that demonstrates all of the available command inputs.  To use the sample, create a new Python or C++ script and copy and paste this code, replacing the default code. You also need to unpack this zip file which contains a [resource folder](../ExtraFiles/CommandInputsResources.zip) into the same folder where the source code file (.py or .cpp) is. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
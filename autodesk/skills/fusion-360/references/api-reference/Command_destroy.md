# Command.destroy Event

Parent Object: [Command](Command.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/Command.h>

## Description

Gets an event that is fired when the command is destroyed. The command is destroyed and can be cleaned up.

## Syntax

* [Python Using fusion360utils](#PythonUsingFusion360Utils)
* [Python](#Python)
* [C++](#C++)

*-------- Import ---------* |

*-------- Global variables ---------* ```` ``` # Global variable used to maintain a reference to all event handlers. handlers = [] ``` ```` *-------- Connect the handler to the event. ---------* ```` ``` # "command_var" is a variable referencing a Command object. # "MyDestroyHandler" is the name of the class that handles the event. onDestroy = MyDestroyHandler() command_var.destroy.add(onDestroy) handlers.append(onDestroy) ``` ```` *-------- Event handler class definition ---------* ```` ``` # Event handler for the destroy event. class MyDestroyHandler(adsk.core.CommandEventHandler):     def __init__(self):         super().__init__()     def notify(self, args: adsk.core.CommandEventArgs):         # Code to react to the event.         app.log('In MyDestroyHandler event handler.') ``` ```` |

*--------- Required include files. ---------* ```` ``` #include <Core/UserInterface/Command.h> #include <Core/UserInterface/CommandEvent.h> #include <Core/UserInterface/CommandEventHandler.h> #include <Core/UserInterface/CommandEventArgs.h> ``` ````  *--------- Event handler class definition and global declaration. --------- ```` ``` // Event handler for the destroy event. ``` ````* class MyDestroyEventHandler : public adsk::core::CommandEventHandler { public:  void notify(const Ptr<CommandEventArgs>& eventArgs) override  {  // Code to react to the event.  ui->messageBox("In MyDestroyEventHandler event handler.");  } } \_destroy;  *--------- Connect the handler to the event. ---------* ```` ``` // "command_var" is a variable referencing a Command object. // Connect the handler function to the event. Ptr<CommandEvent> destroyEvent = command_var->destroy(); if (!destroyEvent)     return;  bool isOk = destroyEvent->add(&_destroy); if (!isOk)     return; ``` ```` |

## Property Value

This is an event property that returns a [CommandEvent](CommandEvent.htm).

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [CommandEvent](CommandEvent.htm) | Returns a CommandEvent object that is used to connect and release from the event. |

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
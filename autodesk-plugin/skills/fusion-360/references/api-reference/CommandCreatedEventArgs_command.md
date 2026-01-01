# CommandCreatedEventArgs.command Property

Parent Object: [CommandCreatedEventArgs](CommandCreatedEventArgs.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/CommandCreatedEventArgs.h>

## Description

Gets the newly created Command object that allows you to perform an action in response to the control being clicked.

## Syntax

* [Python](#Python)
* [C++](#C++)

"commandCreatedEventArgs\_var" is a variable referencing a CommandCreatedEventArgs object. |

"commandCreatedEventArgs\_var" is a variable referencing a CommandCreatedEventArgs object. ```` ``` #include <Core/UserInterface/CommandCreatedEventArgs.h>  // Get the value of the property. Ptr<Command> propertyValue = commandCreatedEventArgs_var->command(); ``` ```` |

## Property Value

This is a read only property whose value is a [Command](Command.htm).

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
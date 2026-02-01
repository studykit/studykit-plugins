# TabCommandInput.children Property

Parent Object: [TabCommandInput](TabCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/TabCommandInput.h>

## Description

Gets the CommandInputs collection for this TabCommandInput. Use the add methods on this collection to add child CommandInputs to this Tab in the desired order.

## Syntax

* [Python](#Python)
* [C++](#C++)

"tabCommandInput\_var" is a variable referencing a TabCommandInput object. |

"tabCommandInput\_var" is a variable referencing a TabCommandInput object. ```` ``` #include <Core/UserInterface/TabCommandInput.h>  // Get the value of the property. Ptr<CommandInputs> propertyValue = tabCommandInput_var->children(); ``` ```` |

## Property Value

This is a read only property whose value is a [CommandInputs](CommandInputs.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Command Inputs API Sample](CommandInputsSample_Sample.htm) | Creates a command dialog that demonstrates all of the available command inputs.  To use the sample, create a new Python or C++ script and copy and paste this code, replacing the default code. You also need to unpack this zip file which contains a [resource folder](../ExtraFiles/CommandInputsResources.zip) into the same folder where the source code file (.py or .cpp) is. |

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
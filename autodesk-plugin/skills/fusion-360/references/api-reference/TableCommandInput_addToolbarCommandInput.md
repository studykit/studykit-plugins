# TableCommandInput.addToolbarCommandInput Method

Parent Object: [TableCommandInput](TableCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/TableCommandInput.h>

## Description

Adds a new command input to the toolbar at the bottom of the table.

## Syntax

* [Python](#Python)
* [C++](#C++)

"tableCommandInput\_var" is a variable referencing a [TableCommandInput](TableCommandInput.htm) object.```` ``` returnValue = tableCommandInput_var.addToolbarCommandInput(input) ``` ```` |

"tableCommandInput\_var" is a variable referencing a [TableCommandInput](TableCommandInput.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the command input was successfully added. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| input | [CommandInput](CommandInput.htm) | Adds a command input to the toolbar at the bottom of the table. The inputs are displayed in the same order that they're added.   The command input is created in the standard way but when it's added to the table using this method it will be displayed in the table instead of the main area of the dialog. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Command Inputs API Sample](CommandInputsSample_Sample.htm) | Creates a command dialog that demonstrates all of the available command inputs.  To use the sample, create a new Python or C++ script and copy and paste this code, replacing the default code. You also need to unpack this zip file which contains a [resource folder](../ExtraFiles/CommandInputsResources.zip) into the same folder where the source code file (.py or .cpp) is. |

## Version

Introduced in version September 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
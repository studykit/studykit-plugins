# CommandInputs.addSeparatorCommandInput Method

Parent Object: [CommandInputs](CommandInputs.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/CommandInputs.h>

## Description

Adds a new Separator input to the command. A separator input is for visual purposes only and creates a line in the dialog providing a visual separation between the command inputs above and below where the separator is inserted.

## Syntax

* [Python](#Python)
* [C++](#C++)

"commandInputs\_var" is a variable referencing a [CommandInputs](CommandInputs.htm) object.```` ``` returnValue = commandInputs_var.addSeparatorCommandInput(id) ``` ```` |

"commandInputs\_var" is a variable referencing a [CommandInputs](CommandInputs.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [SeparatorCommandInput](SeparatorCommandInput.htm) | Returns the created SeparatorCommandInput object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| id | string | The unique ID of this command input. It must be unique with respect to the other inputs associated with this command. |

## Version

Introduced in version May 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
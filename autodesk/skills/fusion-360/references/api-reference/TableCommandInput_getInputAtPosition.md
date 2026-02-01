# TableCommandInput.getInputAtPosition Method

Parent Object: [TableCommandInput](TableCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/TableCommandInput.h>

## Description

Returns the command input that is in the specified row and column. In the case where a command input spans multiple columns, the same input can be returned from multiple positions.

## Syntax

* [Python](#Python)
* [C++](#C++)

"tableCommandInput\_var" is a variable referencing a [TableCommandInput](TableCommandInput.htm) object.```` ``` returnValue = tableCommandInput_var.getInputAtPosition(row, column) ``` ```` |

"tableCommandInput\_var" is a variable referencing a [TableCommandInput](TableCommandInput.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [CommandInput](CommandInput.htm) | Returns the command input that is in the specified row and column. If there isn't a command input in the specified location, null is returned. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| row | integer | The row index to return the command input from where the first row is 0. |
| column | integer | The row index to return the command input from where the first row is 0. |

## Version

Introduced in version November 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
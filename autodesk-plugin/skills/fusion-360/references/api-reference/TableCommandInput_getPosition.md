# TableCommandInput.getPosition Method

Parent Object: [TableCommandInput](TableCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/TableCommandInput.h>

## Description

Gets the position of the specified command input within the table.

## Syntax

* [Python](#Python)
* [C++](#C++)

"tableCommandInput\_var" is a variable referencing a [TableCommandInput](TableCommandInput.htm) object. |

```` ```  #include <Core/UserInterface/TableCommandInput.h ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the position was successfully returned. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| input | [CommandInput](CommandInput.htm) | The existing command input you want to find the associated cell for. |
| row | integer | The returned row index of the cell. |
| column | integer | The returned column index of the cell. |
| rowSpan | integer | The returned number of additional rows used by the input. A value of 0 indicates that no additional rows are used. |
| columnSpan | integer | The returned number of additional columns used by the input. A value of 0 indicates that no additional columns are used. |

## Version

Introduced in version September 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
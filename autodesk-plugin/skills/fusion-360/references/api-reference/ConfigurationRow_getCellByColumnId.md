# ConfigurationRow.getCellByColumnId Method

Parent Object: [ConfigurationRow](ConfigurationRow.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationRow.h>

## Description

Gets the cell in this row at the column with the specified ID.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationRow\_var" is a variable referencing a [ConfigurationRow](ConfigurationRow.htm) object.```` ``` returnValue = configurationRow_var.getCellByColumnId(columnId) ``` ```` |

"configurationRow\_var" is a variable referencing a [ConfigurationRow](ConfigurationRow.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ConfigurationCell](ConfigurationCell.htm) | Returns the specified cell if successful or null if a column with the specified ID does not exist. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| columnId | string | The ID of the column the cell is in. |

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
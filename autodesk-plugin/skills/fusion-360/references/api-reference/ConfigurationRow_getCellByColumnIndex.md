# ConfigurationRow.getCellByColumnIndex Method

Parent Object: [ConfigurationRow](ConfigurationRow.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationRow.h>

## Description

Gets the cell in this row at the specified column index. The first column has an index of 0 and does not include the name column.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationRow\_var" is a variable referencing a [ConfigurationRow](ConfigurationRow.htm) object.```` ``` returnValue = configurationRow_var.getCellByColumnIndex(columnIndex) ``` ```` |

"configurationRow\_var" is a variable referencing a [ConfigurationRow](ConfigurationRow.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ConfigurationCell](ConfigurationCell.htm) | Returns the specified cell if successful and null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| columnIndex | uinteger | The index of the column to return the cell for. The first column has an index 0. |

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
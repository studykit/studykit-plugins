# ConfigurationMaterialTable.getCell Method

Parent Object: [ConfigurationMaterialTable](ConfigurationMaterialTable.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationMaterialTable.h>

## Description

Returns the cell at the specified row and column.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationMaterialTable\_var" is a variable referencing a [ConfigurationMaterialTable](ConfigurationMaterialTable.htm) object.```` ``` returnValue = configurationMaterialTable_var.getCell(column, row) ``` ```` |

"configurationMaterialTable\_var" is a variable referencing a [ConfigurationMaterialTable](ConfigurationMaterialTable.htm) object. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| column | uinteger | The index of the column the cell is in. An index of 0 is the first column and does not include the name column. |
| row | uinteger | The index of the row the cell is in. An index of 0 is the first row and does not include the header row. |

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
# ConfigurationMaterialColumn.getCellByRowId Method

Parent Object: [ConfigurationMaterialColumn](ConfigurationMaterialColumn.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationMaterialColumn.h>

## Description

Gets the cell in this column at the row specified by its ID.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationMaterialColumn\_var" is a variable referencing a [ConfigurationMaterialColumn](ConfigurationMaterialColumn.htm) object.```` ``` returnValue = configurationMaterialColumn_var.getCellByRowId(rowId) ``` ```` |

"configurationMaterialColumn\_var" is a variable referencing a [ConfigurationMaterialColumn](ConfigurationMaterialColumn.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ConfigurationMaterialCell](ConfigurationMaterialCell.htm) | Returns the specified cell if successful and null if the id is not found. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| rowId | string | The ID of the row to return the cell for. |

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
# ConfigurationJointSnapColumn.getCell Method

Parent Object: [ConfigurationJointSnapColumn](ConfigurationJointSnapColumn.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationJointSnapColumn.h>

## Description

Gets the cell in this column at the specified row. Depending on the type of data in the cells within the column a ConfigurationFeatureAspectBooleanCell or ConfigurationFeatureAspectStringCell will be returned. The first row has an index of 0 and does not include the header row.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationJointSnapColumn\_var" is a variable referencing a [ConfigurationJointSnapColumn](ConfigurationJointSnapColumn.htm) object.```` ``` returnValue = configurationJointSnapColumn_var.getCell(rowIndex) ``` ```` |

"configurationJointSnapColumn\_var" is a variable referencing a [ConfigurationJointSnapColumn](ConfigurationJointSnapColumn.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ConfigurationCell](ConfigurationCell.htm) | Returns the specified cell if successful and null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| rowIndex | uinteger | The index of the row to return the cell for. The first row has an index of 0. |

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
# ConfigurationJointSnapColumn.getCellByRowId Method

Parent Object: [ConfigurationJointSnapColumn](ConfigurationJointSnapColumn.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationJointSnapColumn.h>

## Description

This method returns the cell in this column at the row identified by its ID. Depending on the type of data in the cells within the column, a ConfigurationFeatureAspectBooleanCell or ConfigurationFeatureAspectStringCell will be returned.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationJointSnapColumn\_var" is a variable referencing a [ConfigurationJointSnapColumn](ConfigurationJointSnapColumn.htm) object.```` ``` returnValue = configurationJointSnapColumn_var.getCellByRowId(rowId) ``` ```` |

"configurationJointSnapColumn\_var" is a variable referencing a [ConfigurationJointSnapColumn](ConfigurationJointSnapColumn.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ConfigurationCell](ConfigurationCell.htm) | Returns the specified cell if successful and null if the id is not found. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| rowId | string | The ID of the row to return the cell for. |

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
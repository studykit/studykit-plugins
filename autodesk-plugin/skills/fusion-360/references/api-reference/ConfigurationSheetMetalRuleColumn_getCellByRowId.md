# ConfigurationSheetMetalRuleColumn.getCellByRowId Method

Parent Object: [ConfigurationSheetMetalRuleColumn](ConfigurationSheetMetalRuleColumn.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationSheetMetalRuleColumn.h>

## Description

Gets the cell in this column at the row specified by its ID.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationSheetMetalRuleColumn\_var" is a variable referencing a [ConfigurationSheetMetalRuleColumn](ConfigurationSheetMetalRuleColumn.htm) object.```` ``` returnValue = configurationSheetMetalRuleColumn_var.getCellByRowId(rowId) ``` ```` |

"configurationSheetMetalRuleColumn\_var" is a variable referencing a [ConfigurationSheetMetalRuleColumn](ConfigurationSheetMetalRuleColumn.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ConfigurationSheetMetalRuleCell](ConfigurationSheetMetalRuleCell.htm) | Returns the specified cell if successful and null if the id is not found. |

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
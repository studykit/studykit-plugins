# ConfigurationSheetMetalRuleColumns.itemById Method

Parent Object: [ConfigurationSheetMetalRuleColumns](ConfigurationSheetMetalRuleColumns.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationSheetMetalRuleColumns.h>

## Description

A method that returns the column with the specified ID.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationSheetMetalRuleColumns\_var" is a variable referencing a [ConfigurationSheetMetalRuleColumns](ConfigurationSheetMetalRuleColumns.htm) object.```` ``` returnValue = configurationSheetMetalRuleColumns_var.itemById(id) ``` ```` |

"configurationSheetMetalRuleColumns\_var" is a variable referencing a [ConfigurationSheetMetalRuleColumns](ConfigurationSheetMetalRuleColumns.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ConfigurationSheetMetalRuleColumn](ConfigurationSheetMetalRuleColumn.htm) | Returns the specified column or null if a column with the specified ID does not exist. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| id | string | The id of the column to return. |

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
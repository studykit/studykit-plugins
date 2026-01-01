# ConfigurationSheetMetalRuleColumns.item Method

Parent Object: [ConfigurationSheetMetalRuleColumns](ConfigurationSheetMetalRuleColumns.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationSheetMetalRuleColumns.h>

## Description

A method that returns the specified column using an index into the collection. These are returned in the same order as they appear in the table.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationSheetMetalRuleColumns\_var" is a variable referencing a [ConfigurationSheetMetalRuleColumns](ConfigurationSheetMetalRuleColumns.htm) object.```` ``` returnValue = configurationSheetMetalRuleColumns_var.item(index) ``` ```` |

"configurationSheetMetalRuleColumns\_var" is a variable referencing a [ConfigurationSheetMetalRuleColumns](ConfigurationSheetMetalRuleColumns.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ConfigurationSheetMetalRuleColumn](ConfigurationSheetMetalRuleColumn.htm) | Returns the specified column or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the column to return, where the first column is index 0. The name column is not included. |

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
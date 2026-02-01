# ConfigurationSheetMetalRuleColumns.add Method

Parent Object: [ConfigurationSheetMetalRuleColumns](ConfigurationSheetMetalRuleColumns.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationSheetMetalRuleColumns.h>

## Description

Adds a new column to the sheet metal rule table.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationSheetMetalRuleColumns\_var" is a variable referencing a [ConfigurationSheetMetalRuleColumns](ConfigurationSheetMetalRuleColumns.htm) object.```` ``` returnValue = configurationSheetMetalRuleColumns_var.add(component) ``` ```` |

"configurationSheetMetalRuleColumns\_var" is a variable referencing a [ConfigurationSheetMetalRuleColumns](ConfigurationSheetMetalRuleColumns.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ConfigurationSheetMetalRuleColumn](ConfigurationSheetMetalRuleColumn.htm) | Returns the newly created ConfigurationPlasticRuleColumn object or null if it fails. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| component | [Component](Component.htm) | The component whose active sheet metal rule will be controlled by this column. |

## Version

Introduced in version March 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
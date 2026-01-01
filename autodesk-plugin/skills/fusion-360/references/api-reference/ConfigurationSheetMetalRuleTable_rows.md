# ConfigurationSheetMetalRuleTable.rows Property

Parent Object: [ConfigurationSheetMetalRuleTable](ConfigurationSheetMetalRuleTable.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationSheetMetalRuleTable.h>

## Description

Returns the rows (configurations) defined for this table and provides the functionality to create new rows.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationSheetMetalRuleTable\_var" is a variable referencing a ConfigurationSheetMetalRuleTable object. |

"configurationSheetMetalRuleTable\_var" is a variable referencing a ConfigurationSheetMetalRuleTable object. ```` ``` #include <Fusion/Configurations/ConfigurationSheetMetalRuleTable.h>  // Get the value of the property. Ptr<ConfigurationRows> propertyValue = configurationSheetMetalRuleTable_var->rows(); ``` ```` |

## Property Value

This is a read only property whose value is a [ConfigurationRows](ConfigurationRows.htm).

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
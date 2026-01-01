# ConfigurationSheetMetalRuleTable.parentTableColumn Property

Parent Object: [ConfigurationSheetMetalRuleTable](ConfigurationSheetMetalRuleTable.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationSheetMetalRuleTable.h>

## Description

Returns the column in the top table that references this sheet metal rule table.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationSheetMetalRuleTable\_var" is a variable referencing a ConfigurationSheetMetalRuleTable object. |

"configurationSheetMetalRuleTable\_var" is a variable referencing a ConfigurationSheetMetalRuleTable object. ```` ``` #include <Fusion/Configurations/ConfigurationSheetMetalRuleTable.h>  // Get the value of the property. Ptr<ConfigurationThemeColumn> propertyValue = configurationSheetMetalRuleTable_var->parentTableColumn(); ``` ```` |

## Property Value

This is a read only property whose value is a [ConfigurationThemeColumn](ConfigurationThemeColumn.htm).

## Version

Introduced in version March 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
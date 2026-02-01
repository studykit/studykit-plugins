# ConfigurationSheetMetalRuleColumn.componentName Property

Parent Object: [ConfigurationSheetMetalRuleColumn](ConfigurationSheetMetalRuleColumn.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationSheetMetalRuleColumn.h>

## Description

Returns the name of the component associated with this column. This is useful when the table is obtained from a DataFile object, and the component object is unavailable.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationSheetMetalRuleColumn\_var" is a variable referencing a ConfigurationSheetMetalRuleColumn object. |

"configurationSheetMetalRuleColumn\_var" is a variable referencing a ConfigurationSheetMetalRuleColumn object. ```` ``` #include <Fusion/Configurations/ConfigurationSheetMetalRuleColumn.h>  // Get the value of the property. string propertyValue = configurationSheetMetalRuleColumn_var->componentName(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
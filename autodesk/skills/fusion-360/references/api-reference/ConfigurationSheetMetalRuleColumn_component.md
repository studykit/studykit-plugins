# ConfigurationSheetMetalRuleColumn.component Property

Parent Object: [ConfigurationSheetMetalRuleColumn](ConfigurationSheetMetalRuleColumn.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationSheetMetalRuleColumn.h>

## Description

Returns the Component being modified by this column. This property returns null when the table being queried was obtained from a DataFile object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationSheetMetalRuleColumn\_var" is a variable referencing a ConfigurationSheetMetalRuleColumn object. |

"configurationSheetMetalRuleColumn\_var" is a variable referencing a ConfigurationSheetMetalRuleColumn object. ```` ``` #include <Fusion/Configurations/ConfigurationSheetMetalRuleColumn.h>  // Get the value of the property. Ptr<Component> propertyValue = configurationSheetMetalRuleColumn_var->component(); ``` ```` |

## Property Value

This is a read only property whose value is a [Component](Component.htm).

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
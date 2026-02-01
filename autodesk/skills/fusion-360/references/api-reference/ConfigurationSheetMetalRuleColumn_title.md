# ConfigurationSheetMetalRuleColumn.title Property

Parent Object: [ConfigurationSheetMetalRuleColumn](ConfigurationSheetMetalRuleColumn.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationSheetMetalRuleColumn.h>

## Description

The title of this column. In a top table, this can only be edited for suppression, visibility, parameter, and theme table columns. It behaves as read-only for all other types. In a theme table, the title of all the columns can be modified except for the column that represents the root component for materials and appearances.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationSheetMetalRuleColumn\_var" is a variable referencing a ConfigurationSheetMetalRuleColumn object.  ```` ``` # Get the value of the property. propertyValue = configurationSheetMetalRuleColumn_var.title  # Set the value of the property. configurationSheetMetalRuleColumn_var.title = propertyValue ``` ```` |

"configurationSheetMetalRuleColumn\_var" is a variable referencing a ConfigurationSheetMetalRuleColumn object. ```` ``` #include <Fusion/Configurations/ConfigurationSheetMetalRuleColumn.h>  // Get the value of the property. string propertyValue = configurationSheetMetalRuleColumn_var->title();  // Set the value of the property, where value_var is a string. bool returnValue = configurationSheetMetalRuleColumn_var->title(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
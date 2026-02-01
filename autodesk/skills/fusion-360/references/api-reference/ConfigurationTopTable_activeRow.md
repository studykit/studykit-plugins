# ConfigurationTopTable.activeRow Property

Parent Object: [ConfigurationTopTable](ConfigurationTopTable.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationTopTable.h>

## Description

Returns the row that is currently active. To set the active row, use the activate method on the ConfigurationRow object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationTopTable\_var" is a variable referencing a ConfigurationTopTable object. |

"configurationTopTable\_var" is a variable referencing a ConfigurationTopTable object. ```` ``` #include <Fusion/Configurations/ConfigurationTopTable.h>  // Get the value of the property. Ptr<ConfigurationRow> propertyValue = configurationTopTable_var->activeRow(); ``` ```` |

## Property Value

This is a read only property whose value is a [ConfigurationRow](ConfigurationRow.htm).

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
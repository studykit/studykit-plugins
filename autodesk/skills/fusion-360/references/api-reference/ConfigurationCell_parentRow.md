# ConfigurationCell.parentRow Property

Parent Object: [ConfigurationCell](ConfigurationCell.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationCell.h>

## Description

Returns the row this cell is in.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationCell\_var" is a variable referencing a ConfigurationCell object. |

"configurationCell\_var" is a variable referencing a ConfigurationCell object. ```` ``` #include <Fusion/Configurations/ConfigurationCell.h>  // Get the value of the property. Ptr<ConfigurationRow> propertyValue = configurationCell_var->parentRow(); ``` ```` |

## Property Value

This is a read only property whose value is a [ConfigurationRow](ConfigurationRow.htm).

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
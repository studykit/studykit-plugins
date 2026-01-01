# ConfigurationVisibilityCell.parentRow Property

Parent Object: [ConfigurationVisibilityCell](ConfigurationVisibilityCell.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationVisibilityCell.h>

## Description

Returns the row this cell is in.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationVisibilityCell\_var" is a variable referencing a ConfigurationVisibilityCell object. |

"configurationVisibilityCell\_var" is a variable referencing a ConfigurationVisibilityCell object. ```` ``` #include <Fusion/Configurations/ConfigurationVisibilityCell.h>  // Get the value of the property. Ptr<ConfigurationRow> propertyValue = configurationVisibilityCell_var->parentRow(); ``` ```` |

## Property Value

This is a read only property whose value is a [ConfigurationRow](ConfigurationRow.htm).

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
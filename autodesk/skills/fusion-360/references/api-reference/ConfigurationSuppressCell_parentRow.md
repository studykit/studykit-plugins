# ConfigurationSuppressCell.parentRow Property

Parent Object: [ConfigurationSuppressCell](ConfigurationSuppressCell.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationSuppressCell.h>

## Description

Returns the row this cell is in.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationSuppressCell\_var" is a variable referencing a ConfigurationSuppressCell object. |

"configurationSuppressCell\_var" is a variable referencing a ConfigurationSuppressCell object. ```` ``` #include <Fusion/Configurations/ConfigurationSuppressCell.h>  // Get the value of the property. Ptr<ConfigurationRow> propertyValue = configurationSuppressCell_var->parentRow(); ``` ```` |

## Property Value

This is a read only property whose value is a [ConfigurationRow](ConfigurationRow.htm).

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
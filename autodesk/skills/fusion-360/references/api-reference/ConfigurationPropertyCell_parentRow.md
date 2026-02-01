# ConfigurationPropertyCell.parentRow Property

Parent Object: [ConfigurationPropertyCell](ConfigurationPropertyCell.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationPropertyCell.h>

## Description

Returns the row this cell is in.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationPropertyCell\_var" is a variable referencing a ConfigurationPropertyCell object. |

"configurationPropertyCell\_var" is a variable referencing a ConfigurationPropertyCell object. ```` ``` #include <Fusion/Configurations/ConfigurationPropertyCell.h>  // Get the value of the property. Ptr<ConfigurationRow> propertyValue = configurationPropertyCell_var->parentRow(); ``` ```` |

## Property Value

This is a read only property whose value is a [ConfigurationRow](ConfigurationRow.htm).

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
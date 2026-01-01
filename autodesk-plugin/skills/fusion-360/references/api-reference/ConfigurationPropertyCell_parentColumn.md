# ConfigurationPropertyCell.parentColumn Property

Parent Object: [ConfigurationPropertyCell](ConfigurationPropertyCell.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationPropertyCell.h>

## Description

Returns the column this cell is in.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationPropertyCell\_var" is a variable referencing a ConfigurationPropertyCell object. |

"configurationPropertyCell\_var" is a variable referencing a ConfigurationPropertyCell object. ```` ``` #include <Fusion/Configurations/ConfigurationPropertyCell.h>  // Get the value of the property. Ptr<ConfigurationPropertyColumn> propertyValue = configurationPropertyCell_var->parentColumn(); ``` ```` |

## Property Value

This is a read only property whose value is a [ConfigurationPropertyColumn](ConfigurationPropertyColumn.htm).

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
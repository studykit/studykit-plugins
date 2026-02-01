# ConfigurationInsertCell.parentColumn Property

Parent Object: [ConfigurationInsertCell](ConfigurationInsertCell.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationInsertCell.h>

## Description

Returns the column this cell is in.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationInsertCell\_var" is a variable referencing a ConfigurationInsertCell object. |

"configurationInsertCell\_var" is a variable referencing a ConfigurationInsertCell object. ```` ``` #include <Fusion/Configurations/ConfigurationInsertCell.h>  // Get the value of the property. Ptr<ConfigurationInsertColumn> propertyValue = configurationInsertCell_var->parentColumn(); ``` ```` |

## Property Value

This is a read only property whose value is a [ConfigurationInsertColumn](ConfigurationInsertColumn.htm).

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
# ConfigurationThemeCell.parentColumn Property

Parent Object: [ConfigurationThemeCell](ConfigurationThemeCell.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationThemeCell.h>

## Description

Returns the column this cell is in.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationThemeCell\_var" is a variable referencing a ConfigurationThemeCell object. |

"configurationThemeCell\_var" is a variable referencing a ConfigurationThemeCell object. ```` ``` #include <Fusion/Configurations/ConfigurationThemeCell.h>  // Get the value of the property. Ptr<ConfigurationThemeColumn> propertyValue = configurationThemeCell_var->parentColumn(); ``` ```` |

## Property Value

This is a read only property whose value is a [ConfigurationThemeColumn](ConfigurationThemeColumn.htm).

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
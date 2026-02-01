# ConfigurationAppearanceCell.parentColumn Property

Parent Object: [ConfigurationAppearanceCell](ConfigurationAppearanceCell.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationAppearanceCell.h>

## Description

Returns the column this cell is in.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationAppearanceCell\_var" is a variable referencing a ConfigurationAppearanceCell object. |

"configurationAppearanceCell\_var" is a variable referencing a ConfigurationAppearanceCell object. ```` ``` #include <Fusion/Configurations/ConfigurationAppearanceCell.h>  // Get the value of the property. Ptr<ConfigurationAppearanceColumn> propertyValue = configurationAppearanceCell_var->parentColumn(); ``` ```` |

## Property Value

This is a read only property whose value is a [ConfigurationAppearanceColumn](ConfigurationAppearanceColumn.htm).

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
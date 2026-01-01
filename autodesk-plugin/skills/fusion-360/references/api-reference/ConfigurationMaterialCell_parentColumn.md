# ConfigurationMaterialCell.parentColumn Property

Parent Object: [ConfigurationMaterialCell](ConfigurationMaterialCell.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationMaterialCell.h>

## Description

Returns the column this cell is in.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationMaterialCell\_var" is a variable referencing a ConfigurationMaterialCell object. |

"configurationMaterialCell\_var" is a variable referencing a ConfigurationMaterialCell object. ```` ``` #include <Fusion/Configurations/ConfigurationMaterialCell.h>  // Get the value of the property. Ptr<ConfigurationMaterialColumn> propertyValue = configurationMaterialCell_var->parentColumn(); ``` ```` |

## Property Value

This is a read only property whose value is a [ConfigurationMaterialColumn](ConfigurationMaterialColumn.htm).

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
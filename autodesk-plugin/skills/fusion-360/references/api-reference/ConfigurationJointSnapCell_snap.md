# ConfigurationJointSnapCell.snap Property

Parent Object: [ConfigurationJointSnapCell](ConfigurationJointSnapCell.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationJointSnapCell.h>

## Description

Gets and sets which snap will be used when the row this cell is in is active. When setting this property, only snaps defined for the parent column of this cell can be used.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationJointSnapCell\_var" is a variable referencing a ConfigurationJointSnapCell object. |

"configurationJointSnapCell\_var" is a variable referencing a ConfigurationJointSnapCell object. ```` ``` #include <Fusion/Configurations/ConfigurationJointSnapCell.h>  // Get the value of the property. Ptr<ConfigurationJointSnap> propertyValue = configurationJointSnapCell_var->snap();  // Set the value of the property, where value_var is a ConfigurationJointSnap. bool returnValue = configurationJointSnapCell_var->snap(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [ConfigurationJointSnap](ConfigurationJointSnap.htm).

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
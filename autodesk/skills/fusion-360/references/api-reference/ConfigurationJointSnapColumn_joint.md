# ConfigurationJointSnapColumn.joint Property

Parent Object: [ConfigurationJointSnapColumn](ConfigurationJointSnapColumn.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationJointSnapColumn.h>

## Description

Returns the joint or as-built joint being controlled by this column.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationJointSnapColumn\_var" is a variable referencing a ConfigurationJointSnapColumn object.  ```` ``` # Get the value of the property. propertyValue = configurationJointSnapColumn_var.joint ``` ```` |

"configurationJointSnapColumn\_var" is a variable referencing a ConfigurationJointSnapColumn object. ```` ``` #include <Fusion/Configurations/ConfigurationJointSnapColumn.h>  // Get the value of the property. Ptr<Base> propertyValue = configurationJointSnapColumn_var->joint(); ``` ```` |

## Property Value

This is a read only property whose value is a [Base](Base.htm).

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
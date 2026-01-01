# JointOrigin.zAxisEntity Property

Parent Object: [JointOrigin](JointOrigin.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/JointOrigin.h>

## Description

Gets and sets the entity that defines the Z axis direction. This defaults to null meaning the Z axis is inferred from the input geometry.

## Syntax

* [Python](#Python)
* [C++](#C++)

"jointOrigin\_var" is a variable referencing a JointOrigin object.  ```` ``` # Get the value of the property. propertyValue = jointOrigin_var.zAxisEntity  # Set the value of the property. jointOrigin_var.zAxisEntity = propertyValue ``` ```` |

"jointOrigin\_var" is a variable referencing a JointOrigin object. ```` ``` #include <Fusion/Components/JointOrigin.h>  // Get the value of the property. Ptr<Base> propertyValue = jointOrigin_var->zAxisEntity();  // Set the value of the property, where value_var is a Base. bool returnValue = jointOrigin_var->zAxisEntity(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Base](Base.htm).

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
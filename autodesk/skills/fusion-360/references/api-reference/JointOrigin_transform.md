# JointOrigin.transform Property

Parent Object: [JointOrigin](JointOrigin.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/JointOrigin.h>

## Description

Returns the position and orientation of the joint geometry associated with this joint origin. This is returned as a 3D matrix which provides the origin and the X, Y, and Z axis vectors of the coordinate system.

## Syntax

* [Python](#Python)
* [C++](#C++)

"jointOrigin\_var" is a variable referencing a JointOrigin object.  ```` ``` # Get the value of the property. propertyValue = jointOrigin_var.transform ``` ```` |

"jointOrigin\_var" is a variable referencing a JointOrigin object. ```` ``` #include <Fusion/Components/JointOrigin.h>  // Get the value of the property. Ptr<Matrix3D> propertyValue = jointOrigin_var->transform(); ``` ```` |

## Property Value

This is a read only property whose value is a [Matrix3D](Matrix3D.htm).

## Version

Introduced in version November 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
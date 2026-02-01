# Joint.geometryOneTransform Property

Parent Object: [Joint](Joint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/Joint.h>

## Description

Returns the position and orientation of the joint geometry associated with the first occurrence. This is returned as a 3D matrix which provides the origin and the X, Y, and Z axis vectors of the coordinate system.

## Syntax

* [Python](#Python)
* [C++](#C++)

"joint\_var" is a variable referencing a Joint object.  ```` ``` # Get the value of the property. propertyValue = joint_var.geometryOneTransform ``` ```` |

"joint\_var" is a variable referencing a Joint object. ```` ``` #include <Fusion/Components/Joint.h>  // Get the value of the property. Ptr<Matrix3D> propertyValue = joint_var->geometryOneTransform(); ``` ```` |

## Property Value

This is a read only property whose value is a [Matrix3D](Matrix3D.htm).

## Version

Introduced in version November 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
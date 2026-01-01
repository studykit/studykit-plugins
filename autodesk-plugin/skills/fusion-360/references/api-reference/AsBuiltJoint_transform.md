# AsBuiltJoint.transform Property

Parent Object: [AsBuiltJoint](AsBuiltJoint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/AsBuiltJoint.h>

## Description

Returns the position and orientation of the joint geometry associated with this as-built joint. This is returned as a 3D matrix which provides the origin and the X, Y, and Z axis vectors of the coordinate system.

## Syntax

* [Python](#Python)
* [C++](#C++)

"asBuiltJoint\_var" is a variable referencing an AsBuiltJoint object.  ```` ``` # Get the value of the property. propertyValue = asBuiltJoint_var.transform ``` ```` |

"asBuiltJoint\_var" is a variable referencing an AsBuiltJoint object. ```` ``` #include <Fusion/Components/AsBuiltJoint.h>  // Get the value of the property. Ptr<Matrix3D> propertyValue = asBuiltJoint_var->transform(); ``` ```` |

## Property Value

This is a read only property whose value is a [Matrix3D](Matrix3D.htm).

## Version

Introduced in version November 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
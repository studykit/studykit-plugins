# CylindricalJointMotion.rotationAxisVector Property

Parent Object: [CylindricalJointMotion](CylindricalJointMotion.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/CylindricalJointMotion.h>

## Description

Returns the direction of the rotation axis. This property will return null in the case where the CylindricalJointMotion object was obtained from a JointInput object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cylindricalJointMotion\_var" is a variable referencing a CylindricalJointMotion object. |

"cylindricalJointMotion\_var" is a variable referencing a CylindricalJointMotion object. ```` ``` #include <Fusion/Components/CylindricalJointMotion.h>  // Get the value of the property. Ptr<Vector3D> propertyValue = cylindricalJointMotion_var->rotationAxisVector(); ``` ```` |

## Property Value

This is a read only property whose value is a [Vector3D](Vector3D.htm).

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
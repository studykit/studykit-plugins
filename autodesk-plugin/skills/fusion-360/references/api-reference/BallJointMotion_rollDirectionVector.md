# BallJointMotion.rollDirectionVector Property

Parent Object: [BallJointMotion](BallJointMotion.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/BallJointMotion.h>

## Description

Returns the direction that the roll angle is measured from. This property will return null in the case where the BallJointMotion object was obtained from a JointInput object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"ballJointMotion\_var" is a variable referencing a BallJointMotion object. |

"ballJointMotion\_var" is a variable referencing a BallJointMotion object. ```` ``` #include <Fusion/Components/BallJointMotion.h>  // Get the value of the property. Ptr<Vector3D> propertyValue = ballJointMotion_var->rollDirectionVector(); ``` ```` |

## Property Value

This is a read only property whose value is a [Vector3D](Vector3D.htm).

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
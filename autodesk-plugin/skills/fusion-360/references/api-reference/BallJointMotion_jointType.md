# BallJointMotion.jointType Property

Parent Object: [BallJointMotion](BallJointMotion.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/BallJointMotion.h>

## Description

Returns an enum value indicating the type of joint this joint represents.

## Syntax

* [Python](#Python)
* [C++](#C++)

"ballJointMotion\_var" is a variable referencing a BallJointMotion object. |

"ballJointMotion\_var" is a variable referencing a BallJointMotion object. ```` ``` #include <Fusion/Components/BallJointMotion.h>  // Get the value of the property. JointTypes propertyValue = ballJointMotion_var->jointType(); ``` ```` |

## Property Value

This is a read only property whose value is a [JointTypes](JointTypes.htm).

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
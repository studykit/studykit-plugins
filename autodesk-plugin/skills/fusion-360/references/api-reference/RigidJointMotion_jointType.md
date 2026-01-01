# RigidJointMotion.jointType Property

Parent Object: [RigidJointMotion](RigidJointMotion.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/RigidJointMotion.h>

## Description

Returns an enum value indicating the type of joint this joint represents.

## Syntax

* [Python](#Python)
* [C++](#C++)

"rigidJointMotion\_var" is a variable referencing a RigidJointMotion object. |

"rigidJointMotion\_var" is a variable referencing a RigidJointMotion object. ```` ``` #include <Fusion/Components/RigidJointMotion.h>  // Get the value of the property. JointTypes propertyValue = rigidJointMotion_var->jointType(); ``` ```` |

## Property Value

This is a read only property whose value is a [JointTypes](JointTypes.htm).

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
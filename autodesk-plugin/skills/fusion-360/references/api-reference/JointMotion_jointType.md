# JointMotion.jointType Property

Parent Object: [JointMotion](JointMotion.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/JointMotion.h>

## Description

Returns an enum value indicating the type of joint this joint represents.

## Syntax

* [Python](#Python)
* [C++](#C++)

"jointMotion\_var" is a variable referencing a JointMotion object. |

"jointMotion\_var" is a variable referencing a JointMotion object. ```` ``` #include <Fusion/Components/JointMotion.h>  // Get the value of the property. JointTypes propertyValue = jointMotion_var->jointType(); ``` ```` |

## Property Value

This is a read only property whose value is a [JointTypes](JointTypes.htm).

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
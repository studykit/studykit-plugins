# RevoluteJointMotion.jointType Property

Parent Object: [RevoluteJointMotion](RevoluteJointMotion.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/RevoluteJointMotion.h>

## Description

Returns an enum value indicating the type of joint this joint represents.

## Syntax

* [Python](#Python)
* [C++](#C++)

"revoluteJointMotion\_var" is a variable referencing a RevoluteJointMotion object. |

"revoluteJointMotion\_var" is a variable referencing a RevoluteJointMotion object. ```` ``` #include <Fusion/Components/RevoluteJointMotion.h>  // Get the value of the property. JointTypes propertyValue = revoluteJointMotion_var->jointType(); ``` ```` |

## Property Value

This is a read only property whose value is a [JointTypes](JointTypes.htm).

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
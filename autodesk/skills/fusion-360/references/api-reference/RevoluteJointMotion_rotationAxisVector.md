# RevoluteJointMotion.rotationAxisVector Property

Parent Object: [RevoluteJointMotion](RevoluteJointMotion.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/RevoluteJointMotion.h>

## Description

Returns the direction of the rotation axis. This property will return null in the case where the RevolutionJointMotion object was obtained from a JointInput object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"revoluteJointMotion\_var" is a variable referencing a RevoluteJointMotion object. |

"revoluteJointMotion\_var" is a variable referencing a RevoluteJointMotion object. ```` ``` #include <Fusion/Components/RevoluteJointMotion.h>  // Get the value of the property. Ptr<Vector3D> propertyValue = revoluteJointMotion_var->rotationAxisVector(); ``` ```` |

## Property Value

This is a read only property whose value is a [Vector3D](Vector3D.htm).

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
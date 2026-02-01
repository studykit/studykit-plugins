# BallJointMotion.pitchDirection Property

Parent Object: [BallJointMotion](BallJointMotion.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/BallJointMotion.h>

## Description

Gets and sets the direction that the pitch is measured from. This can only be set to ZAxisJointDirection and can return ZAxisJointDirection or CustomJointDirection. If this returns CustomJointDirection then the customNormalDirectionEntity will return an entity that defines the direction. If there is a custom direction defined and this property is set to ZAxisJointDirection, the custom direction will be removed and customNormalDirectionEntity will return null.

## Syntax

* [Python](#Python)
* [C++](#C++)

"ballJointMotion\_var" is a variable referencing a BallJointMotion object. |

"ballJointMotion\_var" is a variable referencing a BallJointMotion object. ```` ``` #include <Fusion/Components/BallJointMotion.h>  // Get the value of the property. JointDirections propertyValue = ballJointMotion_var->pitchDirection();  // Set the value of the property, where value_var is a JointDirections. bool returnValue = ballJointMotion_var->pitchDirection(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [JointDirections](JointDirections.htm).

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
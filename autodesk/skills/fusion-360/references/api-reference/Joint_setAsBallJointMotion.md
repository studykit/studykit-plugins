# Joint.setAsBallJointMotion Method

Parent Object: [Joint](Joint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/Joint.h>

## Description

Redefines the relationship between the two joint geometries as a ball joint.

## Syntax

* [Python](#Python)
* [C++](#C++)

"joint\_var" is a variable referencing a [Joint](Joint.htm) object.```` ``` # Uses no optional arguments. returnValue = joint_var.setAsBallJointMotion(pitchDirection, yawDirection)  # Uses optional arguments. returnValue = joint_var.setAsBallJointMotion(pitchDirection, yawDirection, customPitchDirection, customYawDirection) ``` ```` |

"joint\_var" is a variable referencing a [Joint](Joint.htm) object.  ```` ``` #include <Fusion/Components/Joint.h>  // Uses no optional arguments. returnValue = joint_var->setAsBallJointMotion(pitchDirection, yawDirection);  // Uses optional arguments. returnValue = joint_var->setAsBallJointMotion(pitchDirection, yawDirection, customPitchDirection, customYawDirection); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the operation was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| pitchDirection | [JointDirections](JointDirections.htm) | Defines the direction the pitch angle is measured from. This can be ZAxisJointDirection or CustomJointDirection. If CustomJointDirection is specified then you must also provide a value for the customPitchDirection argument. |
| yawDirection | [JointDirections](JointDirections.htm) | Defines the direction the yaw is measured from. This can be XAxisJointDirection or CustomJointDirection. If CustomJointDirection is specified then you must also provide a value for the customYawDirection argument. |
| customPitchDirection | [Base](Base.htm) | If the pitchDirection argument is customPitchDirection this argument is used to define the direction the pitch angel is measured from. This can be several types of entities that can define a direction.   This is an optional argument whose default value is null. |
| customYawDirection | [Base](Base.htm) | If the yawDirection argument is customPitchDirection this argument is used to define the direction the yaw angel is measured from. This can be several types of entities that can define a direction.   This is an optional argument whose default value is null. |

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
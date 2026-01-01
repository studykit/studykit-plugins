# JointInput.setAsRevoluteJointMotion Method

Parent Object: [JointInput](JointInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/JointInput.h>

## Description

Defines the relationship between the two joint geometries as a revolute joint.

## Syntax

* [Python](#Python)
* [C++](#C++)

"jointInput\_var" is a variable referencing a [JointInput](JointInput.htm) object.```` ``` # Uses no optional arguments. ``` ```` |

"jointInput\_var" is a variable referencing a [JointInput](JointInput.htm) object.  ```` ``` #include <Fusion/Components/JointInput.h>  // Uses no optional arguments. returnValue = jointInput_var->setAsRevoluteJointMotion(rotationAxis);  // Uses optional arguments. returnValue = jointInput_var->setAsRevoluteJointMotion(rotationAxis, customRotationAxisEntity); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the operation was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| rotationAxis | [JointDirections](JointDirections.htm) | Specifies which axis the rotation is around. If this is set to CustomJointDirection then the customRotationAxisEntity argument must also be provided. |
| customRotationAxisEntity | [Base](Base.htm) | If the rotationAxis is customAxisEntity this argument is used to specify the entity that defines the custom axis of rotation. This can be several types of entities that an axis can be derived from.   This is an optional argument whose default value is null. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [RevoluteJointMotion API Sample](RevoluteJointMotionSample_Sample.htm) | Demonstrates creating a joint with revolute joint motion. |

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
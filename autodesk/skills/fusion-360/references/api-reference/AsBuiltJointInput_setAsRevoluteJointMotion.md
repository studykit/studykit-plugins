# AsBuiltJointInput.setAsRevoluteJointMotion Method

Parent Object: [AsBuiltJointInput](AsBuiltJointInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/AsBuiltJointInput.h>

## Description

Defines the relationship between the two joint geometries as a revolute joint.

## Syntax

* [Python](#Python)
* [C++](#C++)

"asBuiltJointInput\_var" is a variable referencing an [AsBuiltJointInput](AsBuiltJointInput.htm) object.```` ``` # Uses no optional arguments. ``` ```` |

"asBuiltJointInput\_var" is a variable referencing an [AsBuiltJointInput](AsBuiltJointInput.htm) object.  ```` ``` #include <Fusion/Components/AsBuiltJointInput.h>  // Uses no optional arguments. returnValue = asBuiltJointInput_var->setAsRevoluteJointMotion(rotationAxis);  // Uses optional arguments. returnValue = asBuiltJointInput_var->setAsRevoluteJointMotion(rotationAxis, customRotationAxisEntity); ``` ```` |

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

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
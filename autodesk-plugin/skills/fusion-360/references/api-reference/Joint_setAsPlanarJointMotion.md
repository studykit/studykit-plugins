# Joint.setAsPlanarJointMotion Method

Parent Object: [Joint](Joint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/Joint.h>

## Description

Redefines the relationship between the two joint geometries as a planar joint.

## Syntax

* [Python](#Python)
* [C++](#C++)

"joint\_var" is a variable referencing a [Joint](Joint.htm) object.```` ``` # Uses no optional arguments. returnValue = joint_var.setAsPlanarJointMotion(normalDirection)  # Uses optional arguments. returnValue = joint_var.setAsPlanarJointMotion(normalDirection, customNormalDirectionEntity, customPrimarySlideDirection) ``` ```` |

"joint\_var" is a variable referencing a [Joint](Joint.htm) object.  ```` ``` #include <Fusion/Components/Joint.h>  // Uses no optional arguments. returnValue = joint_var->setAsPlanarJointMotion(normalDirection);  // Uses optional arguments. returnValue = joint_var->setAsPlanarJointMotion(normalDirection, customNormalDirectionEntity, customPrimarySlideDirection); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the operation was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| normalDirection | [JointDirections](JointDirections.htm) | Defines the direction of the normal of the single degree of rotation. This can be set to XAxisJointDirection, YAxisJointDirection, ZAxisJointDirection, or CustomJointDirection. If set to CustomJointDirection then the customNormalDirectionEntity argument must also be provided. |
| customNormalDirectionEntity | [Base](Base.htm) | If the normalDirection is CustomJointDirection this argument is used to specify the entity that defines the direction of the normal. This can be several types of entities that can define a direction.   This is an optional argument whose default value is null. |
| customPrimarySlideDirection | [Base](Base.htm) | This arguments defines the direction of the primary slide direction. A default primary slide direction is automatically chosen and will be used if this argument is not provided or is null. The secondary slide direction is automatically inferred from the normal and primary slide directions.   This is an optional argument whose default value is null. |

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
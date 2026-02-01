# AsBuiltJoint.setAsCylindricalJointMotion Method

Parent Object: [AsBuiltJoint](AsBuiltJoint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/AsBuiltJoint.h>

## Description

Redefines the relationship between the two joint geometries as a cylindrical joint.

## Syntax

* [Python](#Python)
* [C++](#C++)

"asBuiltJoint\_var" is a variable referencing an [AsBuiltJoint](AsBuiltJoint.htm) object.```` ``` # Uses no optional arguments. returnValue = asBuiltJoint_var.setAsCylindricalJointMotion(rotationAxis)  # Uses optional arguments. returnValue = asBuiltJoint_var.setAsCylindricalJointMotion(rotationAxis, geometry, customRotationAxisEntity) ``` ```` |

"asBuiltJoint\_var" is a variable referencing an [AsBuiltJoint](AsBuiltJoint.htm) object.  ```` ``` #include <Fusion/Components/AsBuiltJoint.h>  // Uses no optional arguments. returnValue = asBuiltJoint_var->setAsCylindricalJointMotion(rotationAxis);  // Uses optional arguments. returnValue = asBuiltJoint_var->setAsCylindricalJointMotion(rotationAxis, geometry, customRotationAxisEntity); ``` ```` |

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
| geometry | [JointGeometry](JointGeometry.htm) | Redefines the joint geometry. If not provided, the existing geometry is used. This argument is required if the current joint motion is rigid.   This is an optional argument whose default value is null. |
| customRotationAxisEntity | [Base](Base.htm) | If the rotationAxis is customAxisEntity this argument is used to specify the entity that defines the custom axis of rotation. This can be several types of entities that an axis can be derived from.   This is an optional argument whose default value is null. |

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
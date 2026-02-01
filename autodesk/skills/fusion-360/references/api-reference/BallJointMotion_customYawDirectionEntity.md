# BallJointMotion.customYawDirectionEntity Property

Parent Object: [BallJointMotion](BallJointMotion.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/BallJointMotion.h>

## Description

This property defines a custom yaw direction and can be set using various types of entities that can infer a direction. For example, a linear edge, sketch line, planar face, and cylindrical face.This property is only valid in the case where the yawDirection property returns CustomJointDirection. Setting this property will automatically set the yawDirection property to CustomJointDirection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"ballJointMotion\_var" is a variable referencing a BallJointMotion object.  ```` ``` # Get the value of the property. propertyValue = ballJointMotion_var.customYawDirectionEntity  # Set the value of the property. ballJointMotion_var.customYawDirectionEntity = propertyValue ``` ```` |

"ballJointMotion\_var" is a variable referencing a BallJointMotion object. ```` ``` #include <Fusion/Components/BallJointMotion.h>  // Get the value of the property. Ptr<Base> propertyValue = ballJointMotion_var->customYawDirectionEntity();  // Set the value of the property, where value_var is a Base. bool returnValue = ballJointMotion_var->customYawDirectionEntity(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Base](Base.htm).

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
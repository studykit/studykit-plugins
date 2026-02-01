# CylindricalJointMotion.customRotationAxisEntity Property

Parent Object: [CylindricalJointMotion](CylindricalJointMotion.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/CylindricalJointMotion.h>

## Description

This property can be set using various types of entities that can infer an axis. For example, a linear edge, sketch line, planar face, and cylindrical face. This property is only valid in the case where the rotationAxis property returns CustomJointDirection. Setting this property will automatically set the rotationAxis property to CustomJointDirection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cylindricalJointMotion\_var" is a variable referencing a CylindricalJointMotion object.  ```` ``` # Get the value of the property. propertyValue = cylindricalJointMotion_var.customRotationAxisEntity  # Set the value of the property. cylindricalJointMotion_var.customRotationAxisEntity = propertyValue ``` ```` |

"cylindricalJointMotion\_var" is a variable referencing a CylindricalJointMotion object. ```` ``` #include <Fusion/Components/CylindricalJointMotion.h>  // Get the value of the property. Ptr<Base> propertyValue = cylindricalJointMotion_var->customRotationAxisEntity();  // Set the value of the property, where value_var is a Base. bool returnValue = cylindricalJointMotion_var->customRotationAxisEntity(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Base](Base.htm).

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
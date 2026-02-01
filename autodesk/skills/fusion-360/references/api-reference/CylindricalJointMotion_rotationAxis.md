# CylindricalJointMotion.rotationAxis Property

Parent Object: [CylindricalJointMotion](CylindricalJointMotion.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/CylindricalJointMotion.h>

## Description

Gets and sets the direction of the axis of rotation. This can be set to XAxisJointDirection, YAxisJointDirection, or ZAxisJointDirection. It can return those three directions and CustomJointDirection. If this returns CustomJointDirection then the customRotationAxisEntity will return an entity that defines the axis. If there is a custom rotation axis defined and this property is set to one of the three standard axes, the custom rotation will be removed and customRotationAxisEntity will return null.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cylindricalJointMotion\_var" is a variable referencing a CylindricalJointMotion object. |

"cylindricalJointMotion\_var" is a variable referencing a CylindricalJointMotion object. ```` ``` #include <Fusion/Components/CylindricalJointMotion.h>  // Get the value of the property. JointDirections propertyValue = cylindricalJointMotion_var->rotationAxis();  // Set the value of the property, where value_var is a JointDirections. bool returnValue = cylindricalJointMotion_var->rotationAxis(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [JointDirections](JointDirections.htm).

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
# PlanarJointMotion.normalDirection Property

Parent Object: [PlanarJointMotion](PlanarJointMotion.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/PlanarJointMotion.h>

## Description

Gets and sets the direction of the normal of the single degree of rotation. This can be set to XAxisJointDirection, YAxisJointDirection, or ZAxisJointDirection. It can return those three directions and CustomJointDirection. If this returns CustomJointDirection then the customNormalDirectionEntity will return an entity that defines the direction. If there is a custom direction defined and this property is set to one of the three standard axes, the custom direction will be removed and customNormalDirectionEntity will return null.

## Syntax

* [Python](#Python)
* [C++](#C++)

"planarJointMotion\_var" is a variable referencing a PlanarJointMotion object. |

"planarJointMotion\_var" is a variable referencing a PlanarJointMotion object. ```` ``` #include <Fusion/Components/PlanarJointMotion.h>  // Get the value of the property. JointDirections propertyValue = planarJointMotion_var->normalDirection();  // Set the value of the property, where value_var is a JointDirections. bool returnValue = planarJointMotion_var->normalDirection(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [JointDirections](JointDirections.htm).

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
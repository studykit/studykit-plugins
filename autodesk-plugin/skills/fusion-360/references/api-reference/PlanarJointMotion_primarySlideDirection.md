# PlanarJointMotion.primarySlideDirection Property

Parent Object: [PlanarJointMotion](PlanarJointMotion.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/PlanarJointMotion.h>

## Description

Gets the direction used as the primary direction for the two translational degrees of freedom. The value of this property is automatically set when setting the normalDirection. When reading this value it can return XAxisJointDirection, YAxisJointDirection, ZAxisJointDirection, or CustomJointDirection. If it's CustomJointDirection then the direction the direction can be determined using the primarySlideDirectionVector and the entity controlling the direction can be get and set using the customPrimarySlideDirectionEntity.

## Syntax

* [Python](#Python)
* [C++](#C++)

"planarJointMotion\_var" is a variable referencing a PlanarJointMotion object. |

"planarJointMotion\_var" is a variable referencing a PlanarJointMotion object. ```` ``` #include <Fusion/Components/PlanarJointMotion.h>  // Get the value of the property. JointDirections propertyValue = planarJointMotion_var->primarySlideDirection(); ``` ```` |

## Property Value

This is a read only property whose value is a [JointDirections](JointDirections.htm).

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
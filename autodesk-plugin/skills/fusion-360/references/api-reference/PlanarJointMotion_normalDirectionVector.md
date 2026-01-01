# PlanarJointMotion.normalDirectionVector Property

Parent Object: [PlanarJointMotion](PlanarJointMotion.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/PlanarJointMotion.h>

## Description

Returns the direction of the normal direction. This property will return null in the case where the PlanarJointMotion object was obtained from a JointInput object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"planarJointMotion\_var" is a variable referencing a PlanarJointMotion object. |

"planarJointMotion\_var" is a variable referencing a PlanarJointMotion object. ```` ``` #include <Fusion/Components/PlanarJointMotion.h>  // Get the value of the property. Ptr<Vector3D> propertyValue = planarJointMotion_var->normalDirectionVector(); ``` ```` |

## Property Value

This is a read only property whose value is a [Vector3D](Vector3D.htm).

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
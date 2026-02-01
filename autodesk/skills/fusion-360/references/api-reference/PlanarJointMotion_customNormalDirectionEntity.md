# PlanarJointMotion.customNormalDirectionEntity Property

Parent Object: [PlanarJointMotion](PlanarJointMotion.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/PlanarJointMotion.h>

## Description

This property defines a custom normal direction and can be set using various types of entities that can infer a direction. For example, a linear edge, sketch line, planar face, and cylindrical face.This property is only valid in the case where the normalDirection property returns CustomJointDirection. Setting this property will automatically set the normalDirection property to CustomJointDirection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"planarJointMotion\_var" is a variable referencing a PlanarJointMotion object.  ```` ``` # Get the value of the property. propertyValue = planarJointMotion_var.customNormalDirectionEntity  # Set the value of the property. planarJointMotion_var.customNormalDirectionEntity = propertyValue ``` ```` |

"planarJointMotion\_var" is a variable referencing a PlanarJointMotion object. ```` ``` #include <Fusion/Components/PlanarJointMotion.h>  // Get the value of the property. Ptr<Base> propertyValue = planarJointMotion_var->customNormalDirectionEntity();  // Set the value of the property, where value_var is a Base. bool returnValue = planarJointMotion_var->customNormalDirectionEntity(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Base](Base.htm).

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
# PlanarJointMotion.customPrimarySlideDirectionEntity Property

Parent Object: [PlanarJointMotion](PlanarJointMotion.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/PlanarJointMotion.h>

## Description

This property can be set using various types of entities that can infer a direction. For example, a linear edge, sketch line, planar face, and cylindrical face. When reading this property, it is only valid in the case where the primarySlideDirection property returns CustomJointDirection. Setting this property will automatically set the primarySlideDirection property to CustomJointDirection. The entity defining the custom direction by be perpendicular to the normal direction.

## Syntax

* [Python](#Python)
* [C++](#C++)

"planarJointMotion\_var" is a variable referencing a PlanarJointMotion object.  ```` ``` # Get the value of the property. propertyValue = planarJointMotion_var.customPrimarySlideDirectionEntity  # Set the value of the property. planarJointMotion_var.customPrimarySlideDirectionEntity = propertyValue ``` ```` |

"planarJointMotion\_var" is a variable referencing a PlanarJointMotion object. ```` ``` #include <Fusion/Components/PlanarJointMotion.h>  // Get the value of the property. Ptr<Base> propertyValue = planarJointMotion_var->customPrimarySlideDirectionEntity();  // Set the value of the property, where value_var is a Base. bool returnValue = planarJointMotion_var->customPrimarySlideDirectionEntity(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Base](Base.htm).

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
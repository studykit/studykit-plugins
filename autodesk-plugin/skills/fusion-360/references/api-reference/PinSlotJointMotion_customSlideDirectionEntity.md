# PinSlotJointMotion.customSlideDirectionEntity Property

Parent Object: [PinSlotJointMotion](PinSlotJointMotion.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/PinSlotJointMotion.h>

## Description

This property can be set using various types of entities that can infer a direction. For example, a linear edge, sketch line, planar face, and cylindrical face. This property is only valid in the case where the slideDirection property returns CustomJointDirection. Setting this property will automatically set the slideDirection property to CustomJointDirection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"pinSlotJointMotion\_var" is a variable referencing a PinSlotJointMotion object.  ```` ``` # Get the value of the property. propertyValue = pinSlotJointMotion_var.customSlideDirectionEntity  # Set the value of the property. pinSlotJointMotion_var.customSlideDirectionEntity = propertyValue ``` ```` |

"pinSlotJointMotion\_var" is a variable referencing a PinSlotJointMotion object. ```` ``` #include <Fusion/Components/PinSlotJointMotion.h>  // Get the value of the property. Ptr<Base> propertyValue = pinSlotJointMotion_var->customSlideDirectionEntity();  // Set the value of the property, where value_var is a Base. bool returnValue = pinSlotJointMotion_var->customSlideDirectionEntity(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Base](Base.htm).

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
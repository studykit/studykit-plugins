# PinSlotJointMotion.rotationValue Property

Parent Object: [PinSlotJointMotion](PinSlotJointMotion.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/PinSlotJointMotion.h>

## Description

Gets and sets the rotation value. This is in radians. Setting this value is the equivalent of using the Drive Joints command.

## Syntax

* [Python](#Python)
* [C++](#C++)

"pinSlotJointMotion\_var" is a variable referencing a PinSlotJointMotion object. |

"pinSlotJointMotion\_var" is a variable referencing a PinSlotJointMotion object. ```` ``` #include <Fusion/Components/PinSlotJointMotion.h>  // Get the value of the property. double propertyValue = pinSlotJointMotion_var->rotationValue();  // Set the value of the property, where value_var is a double. bool returnValue = pinSlotJointMotion_var->rotationValue(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
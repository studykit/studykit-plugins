# PinSlotJointMotion.slideLimits Property

Parent Object: [PinSlotJointMotion](PinSlotJointMotion.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/PinSlotJointMotion.h>

## Description

Returns a JointLimits object that defines the slide limits for this joint. Use the functionality of the returned JointLimits object to get, set, and modify the joint limits.

## Syntax

* [Python](#Python)
* [C++](#C++)

"pinSlotJointMotion\_var" is a variable referencing a PinSlotJointMotion object. |

"pinSlotJointMotion\_var" is a variable referencing a PinSlotJointMotion object. ```` ``` #include <Fusion/Components/PinSlotJointMotion.h>  // Get the value of the property. Ptr<JointLimits> propertyValue = pinSlotJointMotion_var->slideLimits(); ``` ```` |

## Property Value

This is a read only property whose value is a [JointLimits](JointLimits.htm).

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
# CylindricalJointMotion.rotationLimits Property

Parent Object: [CylindricalJointMotion](CylindricalJointMotion.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/CylindricalJointMotion.h>

## Description

Returns a JointLimits object that defines the rotation limits for this joint. Use the functionality of the returned JointLimits object to get, set, and modify the joint limits.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cylindricalJointMotion\_var" is a variable referencing a CylindricalJointMotion object. |

"cylindricalJointMotion\_var" is a variable referencing a CylindricalJointMotion object. ```` ``` #include <Fusion/Components/CylindricalJointMotion.h>  // Get the value of the property. Ptr<JointLimits> propertyValue = cylindricalJointMotion_var->rotationLimits(); ``` ```` |

## Property Value

This is a read only property whose value is a [JointLimits](JointLimits.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [CylindricalJointMotion API Sample](CylindricalJointMotionSample_Sample.htm) | Demonstrates creating a joint with cylindrical joint motion. |

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
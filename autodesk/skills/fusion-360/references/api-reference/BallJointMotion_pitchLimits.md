# BallJointMotion.pitchLimits Property

Parent Object: [BallJointMotion](BallJointMotion.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/BallJointMotion.h>

## Description

Returns a JointLimits object that defines the limits of rotation for the pitch. Use the functionality of the returned JointLimits object to get, set, and modify the joint limits.

## Syntax

* [Python](#Python)
* [C++](#C++)

"ballJointMotion\_var" is a variable referencing a BallJointMotion object. |

"ballJointMotion\_var" is a variable referencing a BallJointMotion object. ```` ``` #include <Fusion/Components/BallJointMotion.h>  // Get the value of the property. Ptr<JointLimits> propertyValue = ballJointMotion_var->pitchLimits(); ``` ```` |

## Property Value

This is a read only property whose value is a [JointLimits](JointLimits.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [BallJointMotion API Sample](BallJointMotionSample_Sample.htm) | Demonstrates creating a joint with ball joint motion |

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
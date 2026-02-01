# RevoluteJointMotion.rotationLimits Property

Parent Object: [RevoluteJointMotion](RevoluteJointMotion.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/RevoluteJointMotion.h>

## Description

Returns a JointLimits object that defines the rotation limits for this joint. Use the functionality of the returned JointLimits object to get, set, and modify the joint limits.

## Syntax

* [Python](#Python)
* [C++](#C++)

"revoluteJointMotion\_var" is a variable referencing a RevoluteJointMotion object. |

"revoluteJointMotion\_var" is a variable referencing a RevoluteJointMotion object. ```` ``` #include <Fusion/Components/RevoluteJointMotion.h>  // Get the value of the property. Ptr<JointLimits> propertyValue = revoluteJointMotion_var->rotationLimits(); ``` ```` |

## Property Value

This is a read only property whose value is a [JointLimits](JointLimits.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [RevoluteJointMotion API Sample](RevoluteJointMotionSample_Sample.htm) | Demonstrates creating a joint with revolute joint motion. |

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
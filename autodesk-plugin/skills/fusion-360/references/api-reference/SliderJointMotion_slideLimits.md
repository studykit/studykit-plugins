# SliderJointMotion.slideLimits Property

Parent Object: [SliderJointMotion](SliderJointMotion.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/SliderJointMotion.h>

## Description

Returns a JointLimits object that defines the slide limits for this joint. Use the functionality of the returned JointLimits object to get, set, and modify the joint limits.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sliderJointMotion\_var" is a variable referencing a SliderJointMotion object. |

"sliderJointMotion\_var" is a variable referencing a SliderJointMotion object. ```` ``` #include <Fusion/Components/SliderJointMotion.h>  // Get the value of the property. Ptr<JointLimits> propertyValue = sliderJointMotion_var->slideLimits(); ``` ```` |

## Property Value

This is a read only property whose value is a [JointLimits](JointLimits.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [SliderJointMotion API Sample](SliderJointMotionSample_Sample.htm) | Demonstrates creating a joint with slider joint motion. |

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
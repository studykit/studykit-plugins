# JointLimits.isMaximumValueEnabled Property

Parent Object: [JointLimits](JointLimits.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/JointLimits.h>

## Description

Gets and sets whether the maximum joint limit is enabled or not.

## Syntax

* [Python](#Python)
* [C++](#C++)

"jointLimits\_var" is a variable referencing a JointLimits object. |

"jointLimits\_var" is a variable referencing a JointLimits object. ```` ``` #include <Fusion/Components/JointLimits.h>  // Get the value of the property. boolean propertyValue = jointLimits_var->isMaximumValueEnabled();  // Set the value of the property, where value_var is a boolean. bool returnValue = jointLimits_var->isMaximumValueEnabled(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

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
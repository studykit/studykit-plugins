# PlanarJointMotion.rotationLimits Property

Parent Object: [PlanarJointMotion](PlanarJointMotion.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/PlanarJointMotion.h>

## Description

Returns a JointLimits object that defines the limits of rotation for this joint. Use the functionality of the returned JointLimits object to get, set, and modify the joint limits.

## Syntax

* [Python](#Python)
* [C++](#C++)

"planarJointMotion\_var" is a variable referencing a PlanarJointMotion object. |

"planarJointMotion\_var" is a variable referencing a PlanarJointMotion object. ```` ``` #include <Fusion/Components/PlanarJointMotion.h>  // Get the value of the property. Ptr<JointLimits> propertyValue = planarJointMotion_var->rotationLimits(); ``` ```` |

## Property Value

This is a read only property whose value is a [JointLimits](JointLimits.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Planar Joint Motion API Sample](PlanarJointMotionSample_Sample.htm) | Demonstrates creating a joint with planar joint motion |

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
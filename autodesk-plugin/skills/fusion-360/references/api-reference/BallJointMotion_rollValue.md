# BallJointMotion.rollValue Property

Parent Object: [BallJointMotion](BallJointMotion.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/BallJointMotion.h>

## Description

Gets and sets the roll value. This is in radians. Setting this value is the equivalent of using the Drive Joints command.

## Syntax

* [Python](#Python)
* [C++](#C++)

"ballJointMotion\_var" is a variable referencing a BallJointMotion object. |

"ballJointMotion\_var" is a variable referencing a BallJointMotion object. ```` ``` #include <Fusion/Components/BallJointMotion.h>  // Get the value of the property. double propertyValue = ballJointMotion_var->rollValue();  // Set the value of the property, where value_var is a double. bool returnValue = ballJointMotion_var->rollValue(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
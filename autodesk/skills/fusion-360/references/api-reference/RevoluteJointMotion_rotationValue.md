# RevoluteJointMotion.rotationValue Property

Parent Object: [RevoluteJointMotion](RevoluteJointMotion.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/RevoluteJointMotion.h>

## Description

Gets and sets the rotation value. This is in radians. Setting this value is the equivalent of using the Drive Joints command.

## Syntax

* [Python](#Python)
* [C++](#C++)

"revoluteJointMotion\_var" is a variable referencing a RevoluteJointMotion object. |

"revoluteJointMotion\_var" is a variable referencing a RevoluteJointMotion object. ```` ``` #include <Fusion/Components/RevoluteJointMotion.h>  // Get the value of the property. double propertyValue = revoluteJointMotion_var->rotationValue();  // Set the value of the property, where value_var is a double. bool returnValue = revoluteJointMotion_var->rotationValue(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
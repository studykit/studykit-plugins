# PlanarJointMotion.primarySlideValue Property

Parent Object: [PlanarJointMotion](PlanarJointMotion.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/PlanarJointMotion.h>

## Description

Gets and sets the offset value in the primary direction. This is in centimeters. Setting this value is the equivalent of using the Drive Joints command.

## Syntax

* [Python](#Python)
* [C++](#C++)

"planarJointMotion\_var" is a variable referencing a PlanarJointMotion object. |

"planarJointMotion\_var" is a variable referencing a PlanarJointMotion object. ```` ``` #include <Fusion/Components/PlanarJointMotion.h>  // Get the value of the property. double propertyValue = planarJointMotion_var->primarySlideValue();  // Set the value of the property, where value_var is a double. bool returnValue = planarJointMotion_var->primarySlideValue(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
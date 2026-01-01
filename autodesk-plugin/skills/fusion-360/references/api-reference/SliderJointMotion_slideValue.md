# SliderJointMotion.slideValue Property

Parent Object: [SliderJointMotion](SliderJointMotion.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/SliderJointMotion.h>

## Description

Gets and sets the slide value. This is in centimeters. Setting this value is the equivalent of using the Drive Joints command.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sliderJointMotion\_var" is a variable referencing a SliderJointMotion object. |

"sliderJointMotion\_var" is a variable referencing a SliderJointMotion object. ```` ``` #include <Fusion/Components/SliderJointMotion.h>  // Get the value of the property. double propertyValue = sliderJointMotion_var->slideValue();  // Set the value of the property, where value_var is a double. bool returnValue = sliderJointMotion_var->slideValue(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
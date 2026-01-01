# SliderJointMotion.slideDirection Property

Parent Object: [SliderJointMotion](SliderJointMotion.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/SliderJointMotion.h>

## Description

Gets and sets the direction of the slide. This can be set to XAxisJointDirection, YAxisJointDirection, or ZAxisJointDirection. It can return those three directions and CustomJointDirection. If this returns CustomJointDirection then the customSlideDirectionEntity will return an entity that defines the direction. If there is a custom direction defined and this property is set to one of the three standard axes, the custom direction will be removed and customSlideDirectionEntity will return null.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sliderJointMotion\_var" is a variable referencing a SliderJointMotion object. |

"sliderJointMotion\_var" is a variable referencing a SliderJointMotion object. ```` ``` #include <Fusion/Components/SliderJointMotion.h>  // Get the value of the property. JointDirections propertyValue = sliderJointMotion_var->slideDirection();  // Set the value of the property, where value_var is a JointDirections. bool returnValue = sliderJointMotion_var->slideDirection(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [JointDirections](JointDirections.htm).

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
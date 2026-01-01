# SliderJointMotion.slideDirectionVector Property

Parent Object: [SliderJointMotion](SliderJointMotion.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/SliderJointMotion.h>

## Description

Returns the direction of the slide. This property will return null in the case where the SliderJointMotion object was obtained from a JointInput object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sliderJointMotion\_var" is a variable referencing a SliderJointMotion object. |

"sliderJointMotion\_var" is a variable referencing a SliderJointMotion object. ```` ``` #include <Fusion/Components/SliderJointMotion.h>  // Get the value of the property. Ptr<Vector3D> propertyValue = sliderJointMotion_var->slideDirectionVector(); ``` ```` |

## Property Value

This is a read only property whose value is a [Vector3D](Vector3D.htm).

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
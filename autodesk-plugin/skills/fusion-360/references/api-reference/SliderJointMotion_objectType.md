# SliderJointMotion.objectType Property

Parent Object: [SliderJointMotion](SliderJointMotion.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/SliderJointMotion.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sliderJointMotion\_var" is a variable referencing a SliderJointMotion object.  ```` ``` # Get the value of the property. propertyValue = sliderJointMotion_var.objectType ``` ```` |

"sliderJointMotion\_var" is a variable referencing a SliderJointMotion object. ```` ``` #include <Fusion/Components/SliderJointMotion.h>  // Get the value of the property. string propertyValue = sliderJointMotion_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
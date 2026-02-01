# RectangularPatternFeatureInput.directionOneEntity Property

Parent Object: [RectangularPatternFeatureInput](RectangularPatternFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/RectangularPatternFeatureInput.h>

## Description

Gets and sets the first direction entity. This can be a linear edge, construction axis, sketch line or rectangular pattern feature. If a rectangular pattern feature is set, the directionOneEntity and directionTwoEntity properties return the same rectangular pattern feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"rectangularPatternFeatureInput\_var" is a variable referencing a RectangularPatternFeatureInput object. |

"rectangularPatternFeatureInput\_var" is a variable referencing a RectangularPatternFeatureInput object. ```` ``` #include <Fusion/Features/RectangularPatternFeatureInput.h>  // Get the value of the property. Ptr<Base> propertyValue = rectangularPatternFeatureInput_var->directionOneEntity();  // Set the value of the property, where value_var is a Base. bool returnValue = rectangularPatternFeatureInput_var->directionOneEntity(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Base](Base.htm).

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
# RectangularPatternFeatureInput.patternDistanceType Property

Parent Object: [RectangularPatternFeatureInput](RectangularPatternFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/RectangularPatternFeatureInput.h>

## Description

Gets and sets how the distance between elements is computed.

## Syntax

* [Python](#Python)
* [C++](#C++)

"rectangularPatternFeatureInput\_var" is a variable referencing a RectangularPatternFeatureInput object. |

"rectangularPatternFeatureInput\_var" is a variable referencing a RectangularPatternFeatureInput object. ```` ``` #include <Fusion/Features/RectangularPatternFeatureInput.h>  // Get the value of the property. PatternDistanceType propertyValue = rectangularPatternFeatureInput_var->patternDistanceType();  // Set the value of the property, where value_var is a PatternDistanceType. bool returnValue = rectangularPatternFeatureInput_var->patternDistanceType(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [PatternDistanceType](PatternDistanceType.htm).

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
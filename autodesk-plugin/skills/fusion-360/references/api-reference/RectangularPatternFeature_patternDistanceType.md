# RectangularPatternFeature.patternDistanceType Property

Parent Object: [RectangularPatternFeature](RectangularPatternFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/RectangularPatternFeature.h>

## Description

Gets and sets how the distance between elements is computed. Is initialized to ExtentPatternDistanceType when a new RectangularPatternFeatureInput has been created.

## Syntax

* [Python](#Python)
* [C++](#C++)

"rectangularPatternFeature\_var" is a variable referencing a RectangularPatternFeature object.  ```` ``` # Get the value of the property. propertyValue = rectangularPatternFeature_var.patternDistanceType  # Set the value of the property. rectangularPatternFeature_var.patternDistanceType = propertyValue ``` ```` |

"rectangularPatternFeature\_var" is a variable referencing a RectangularPatternFeature object. ```` ``` #include <Fusion/Features/RectangularPatternFeature.h>  // Get the value of the property. PatternDistanceType propertyValue = rectangularPatternFeature_var->patternDistanceType();  // Set the value of the property, where value_var is a PatternDistanceType. bool returnValue = rectangularPatternFeature_var->patternDistanceType(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [PatternDistanceType](PatternDistanceType.htm).

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
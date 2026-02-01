# PathPatternFeatureInput.patternDistanceType Property

Parent Object: [PathPatternFeatureInput](PathPatternFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/PathPatternFeatureInput.h>

## Description

Gets and sets how the distance between elements is computed.

## Syntax

* [Python](#Python)
* [C++](#C++)

"pathPatternFeatureInput\_var" is a variable referencing a PathPatternFeatureInput object. |

"pathPatternFeatureInput\_var" is a variable referencing a PathPatternFeatureInput object. ```` ``` #include <Fusion/Features/PathPatternFeatureInput.h>  // Get the value of the property. PatternDistanceType propertyValue = pathPatternFeatureInput_var->patternDistanceType();  // Set the value of the property, where value_var is a PatternDistanceType. bool returnValue = pathPatternFeatureInput_var->patternDistanceType(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [PatternDistanceType](PatternDistanceType.htm).

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
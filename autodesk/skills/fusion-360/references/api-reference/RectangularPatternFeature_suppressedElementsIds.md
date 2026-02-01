# RectangularPatternFeature.suppressedElementsIds Property

Parent Object: [RectangularPatternFeature](RectangularPatternFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/RectangularPatternFeature.h>

## Description

Gets and sets the ids of the patterns to suppress.

## Syntax

* [Python](#Python)
* [C++](#C++)

"rectangularPatternFeature\_var" is a variable referencing a RectangularPatternFeature object.  ```` ``` # Get the value of the property. propertyValue = rectangularPatternFeature_var.suppressedElementsIds  # Set the value of the property. rectangularPatternFeature_var.suppressedElementsIds = propertyValue ``` ```` |

"rectangularPatternFeature\_var" is a variable referencing a RectangularPatternFeature object. ```` ``` #include <Fusion/Features/RectangularPatternFeature.h>  // Get the value of the property. std::vector<uinteger> propertyValue = rectangularPatternFeature_var->suppressedElementsIds();  // Set the value of the property, where value_var is a uinteger. bool returnValue = rectangularPatternFeature_var->suppressedElementsIds(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an array of type uinteger.

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
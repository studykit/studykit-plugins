# CircularPatternFeature.suppressedElementsIds Property

Parent Object: [CircularPatternFeature](CircularPatternFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/CircularPatternFeature.h>

## Description

Gets and sets the id's of the elements to suppress.

## Syntax

* [Python](#Python)
* [C++](#C++)

"circularPatternFeature\_var" is a variable referencing a CircularPatternFeature object.  ```` ``` # Get the value of the property. propertyValue = circularPatternFeature_var.suppressedElementsIds  # Set the value of the property. circularPatternFeature_var.suppressedElementsIds = propertyValue ``` ```` |

"circularPatternFeature\_var" is a variable referencing a CircularPatternFeature object. ```` ``` #include <Fusion/Features/CircularPatternFeature.h>  // Get the value of the property. std::vector<uinteger> propertyValue = circularPatternFeature_var->suppressedElementsIds();  // Set the value of the property, where value_var is a uinteger. bool returnValue = circularPatternFeature_var->suppressedElementsIds(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an array of type uinteger.

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
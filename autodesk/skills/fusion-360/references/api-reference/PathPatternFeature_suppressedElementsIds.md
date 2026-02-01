# PathPatternFeature.suppressedElementsIds Property

Parent Object: [PathPatternFeature](PathPatternFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/PathPatternFeature.h>

## Description

Gets and sets the id's of the elements to suppress.

## Syntax

* [Python](#Python)
* [C++](#C++)

"pathPatternFeature\_var" is a variable referencing a PathPatternFeature object.  ```` ``` # Get the value of the property. propertyValue = pathPatternFeature_var.suppressedElementsIds  # Set the value of the property. pathPatternFeature_var.suppressedElementsIds = propertyValue ``` ```` |

"pathPatternFeature\_var" is a variable referencing a PathPatternFeature object. ```` ``` #include <Fusion/Features/PathPatternFeature.h>  // Get the value of the property. std::vector<uinteger> propertyValue = pathPatternFeature_var->suppressedElementsIds();  // Set the value of the property, where value_var is a uinteger. bool returnValue = pathPatternFeature_var->suppressedElementsIds(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an array of type uinteger.

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
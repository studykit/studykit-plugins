# PathPatternFeature.startPoint Property

Parent Object: [PathPatternFeature](PathPatternFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/PathPatternFeature.h>

## Description

Gets and sets the start point on the path to count the distance. It's between 0 and 1. 0 means start point of the path, 1 means end point of the path.

## Syntax

* [Python](#Python)
* [C++](#C++)

"pathPatternFeature\_var" is a variable referencing a PathPatternFeature object.  ```` ``` # Get the value of the property. propertyValue = pathPatternFeature_var.startPoint  # Set the value of the property. pathPatternFeature_var.startPoint = propertyValue ``` ```` |

"pathPatternFeature\_var" is a variable referencing a PathPatternFeature object. ```` ``` #include <Fusion/Features/PathPatternFeature.h>  // Get the value of the property. double propertyValue = pathPatternFeature_var->startPoint();  // Set the value of the property, where value_var is a double. bool returnValue = pathPatternFeature_var->startPoint(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
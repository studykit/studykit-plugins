# PathPatternFeature.isOrientationAlongPath Property

Parent Object: [PathPatternFeature](PathPatternFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/PathPatternFeature.h>

## Description

Gets and sets if the orientation is along path. If false, the orientation is identical.

## Syntax

* [Python](#Python)
* [C++](#C++)

"pathPatternFeature\_var" is a variable referencing a PathPatternFeature object.  ```` ``` # Get the value of the property. propertyValue = pathPatternFeature_var.isOrientationAlongPath  # Set the value of the property. pathPatternFeature_var.isOrientationAlongPath = propertyValue ``` ```` |

"pathPatternFeature\_var" is a variable referencing a PathPatternFeature object. ```` ``` #include <Fusion/Features/PathPatternFeature.h>  // Get the value of the property. boolean propertyValue = pathPatternFeature_var->isOrientationAlongPath();  // Set the value of the property, where value_var is a boolean. bool returnValue = pathPatternFeature_var->isOrientationAlongPath(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
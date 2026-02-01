# PathPatternFeature.path Property

Parent Object: [PathPatternFeature](PathPatternFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/PathPatternFeature.h>

## Description

Gets and sets the path to create the pattern on path.

## Syntax

* [Python](#Python)
* [C++](#C++)

"pathPatternFeature\_var" is a variable referencing a PathPatternFeature object.  ```` ``` # Get the value of the property. propertyValue = pathPatternFeature_var.path  # Set the value of the property. pathPatternFeature_var.path = propertyValue ``` ```` |

"pathPatternFeature\_var" is a variable referencing a PathPatternFeature object. ```` ``` #include <Fusion/Features/PathPatternFeature.h>  // Get the value of the property. Ptr<Path> propertyValue = pathPatternFeature_var->path();  // Set the value of the property, where value_var is a Path. bool returnValue = pathPatternFeature_var->path(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Path](Path.htm).

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
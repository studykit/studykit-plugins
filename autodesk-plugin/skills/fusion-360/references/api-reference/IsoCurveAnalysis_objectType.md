# IsoCurveAnalysis.objectType Property

Parent Object: [IsoCurveAnalysis](IsoCurveAnalysis.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/IsoCurveAnalysis.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"isoCurveAnalysis\_var" is a variable referencing an IsoCurveAnalysis object.  ```` ``` # Get the value of the property. propertyValue = isoCurveAnalysis_var.objectType ``` ```` |

"isoCurveAnalysis\_var" is a variable referencing an IsoCurveAnalysis object. ```` ``` #include <Fusion/Fusion/IsoCurveAnalysis.h>  // Get the value of the property. string propertyValue = isoCurveAnalysis_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
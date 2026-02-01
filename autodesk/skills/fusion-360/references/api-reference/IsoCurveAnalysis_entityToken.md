# IsoCurveAnalysis.entityToken Property

Parent Object: [IsoCurveAnalysis](IsoCurveAnalysis.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/IsoCurveAnalysis.h>

## Description

Returns a token for the Analysis object. The token can be saved and used later with the Design.findEntityByToken method to get back the same Analysis.

## Syntax

* [Python](#Python)
* [C++](#C++)

"isoCurveAnalysis\_var" is a variable referencing an IsoCurveAnalysis object.  ```` ``` # Get the value of the property. propertyValue = isoCurveAnalysis_var.entityToken ``` ```` |

"isoCurveAnalysis\_var" is a variable referencing an IsoCurveAnalysis object. ```` ``` #include <Fusion/Fusion/IsoCurveAnalysis.h>  // Get the value of the property. string propertyValue = isoCurveAnalysis_var->entityToken(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
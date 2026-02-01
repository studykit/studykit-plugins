# CurvatureCombAnalysis.entityToken Property

Parent Object: [CurvatureCombAnalysis](CurvatureCombAnalysis.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/CurvatureCombAnalysis.h>

## Description

Returns a token for the Analysis object. The token can be saved and used later with the Design.findEntityByToken method to get back the same Analysis.

## Syntax

* [Python](#Python)
* [C++](#C++)

"curvatureCombAnalysis\_var" is a variable referencing a CurvatureCombAnalysis object.  ```` ``` # Get the value of the property. propertyValue = curvatureCombAnalysis_var.entityToken ``` ```` |

"curvatureCombAnalysis\_var" is a variable referencing a CurvatureCombAnalysis object. ```` ``` #include <Fusion/Fusion/CurvatureCombAnalysis.h>  // Get the value of the property. string propertyValue = curvatureCombAnalysis_var->entityToken(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
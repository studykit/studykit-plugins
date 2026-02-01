# CurvatureMapAnalysis.entityToken Property

Parent Object: [CurvatureMapAnalysis](CurvatureMapAnalysis.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/CurvatureMapAnalysis.h>

## Description

Returns a token for the Analysis object. The token can be saved and used later with the Design.findEntityByToken method to get back the same Analysis.

## Syntax

* [Python](#Python)
* [C++](#C++)

"curvatureMapAnalysis\_var" is a variable referencing a CurvatureMapAnalysis object.  ```` ``` # Get the value of the property. propertyValue = curvatureMapAnalysis_var.entityToken ``` ```` |

"curvatureMapAnalysis\_var" is a variable referencing a CurvatureMapAnalysis object. ```` ``` #include <Fusion/Fusion/CurvatureMapAnalysis.h>  // Get the value of the property. string propertyValue = curvatureMapAnalysis_var->entityToken(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
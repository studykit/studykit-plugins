# CurvatureMapAnalysis.isVisible Property

Parent Object: [CurvatureMapAnalysis](CurvatureMapAnalysis.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/CurvatureMapAnalysis.h>

## Description

Gets if this Analysis is currently visible in the graphics window. The visibility is controlled by a combination of the isLightBulbOn properties of the Analyses collection object and the Analysis object. If both are true, the Analysis will be visible.

## Syntax

* [Python](#Python)
* [C++](#C++)

"curvatureMapAnalysis\_var" is a variable referencing a CurvatureMapAnalysis object. |

"curvatureMapAnalysis\_var" is a variable referencing a CurvatureMapAnalysis object. ```` ``` #include <Fusion/Fusion/CurvatureMapAnalysis.h>  // Get the value of the property. boolean propertyValue = curvatureMapAnalysis_var->isVisible(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version January 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
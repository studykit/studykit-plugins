# Analyses.isoCurveAnalyses Property

Parent Object: [Analyses](Analyses.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/Analyses.h>

## Description

Returns the IsoCurveAnalyses object, which provides access to any existing IsoCurveAnalysis objects in the design.

## Syntax

* [Python](#Python)
* [C++](#C++)

"analyses\_var" is a variable referencing an Analyses object. |

"analyses\_var" is a variable referencing an Analyses object. ```` ``` #include <Fusion/Fusion/Analyses.h>  // Get the value of the property. Ptr<IsoCurveAnalyses> propertyValue = analyses_var->isoCurveAnalyses(); ``` ```` |

## Property Value

This is a read only property whose value is an [IsoCurveAnalyses](IsoCurveAnalyses.htm).

## Version

Introduced in version January 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
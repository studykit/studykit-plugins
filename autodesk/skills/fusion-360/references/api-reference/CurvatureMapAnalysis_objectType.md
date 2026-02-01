# CurvatureMapAnalysis.objectType Property

Parent Object: [CurvatureMapAnalysis](CurvatureMapAnalysis.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/CurvatureMapAnalysis.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"curvatureMapAnalysis\_var" is a variable referencing a CurvatureMapAnalysis object.  ```` ``` # Get the value of the property. propertyValue = curvatureMapAnalysis_var.objectType ``` ```` |

"curvatureMapAnalysis\_var" is a variable referencing a CurvatureMapAnalysis object. ```` ``` #include <Fusion/Fusion/CurvatureMapAnalysis.h>  // Get the value of the property. string propertyValue = curvatureMapAnalysis_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
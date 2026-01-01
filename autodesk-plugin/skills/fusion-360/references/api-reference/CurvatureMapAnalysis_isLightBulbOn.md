# CurvatureMapAnalysis.isLightBulbOn Property

Parent Object: [CurvatureMapAnalysis](CurvatureMapAnalysis.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/CurvatureMapAnalysis.h>

## Description

A property that gets and sets if the display is enabled for this Analysis object. If false, this analysis will be hidden. If true and the IsLightBulbOn property of the Analyses object is True the Analysis will be visible.

## Syntax

* [Python](#Python)
* [C++](#C++)

"curvatureMapAnalysis\_var" is a variable referencing a CurvatureMapAnalysis object. |

"curvatureMapAnalysis\_var" is a variable referencing a CurvatureMapAnalysis object. ```` ``` #include <Fusion/Fusion/CurvatureMapAnalysis.h>  // Get the value of the property. boolean propertyValue = curvatureMapAnalysis_var->isLightBulbOn();  // Set the value of the property, where value_var is a boolean. bool returnValue = curvatureMapAnalysis_var->isLightBulbOn(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version January 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
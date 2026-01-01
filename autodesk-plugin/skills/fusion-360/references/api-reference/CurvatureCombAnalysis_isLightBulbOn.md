# CurvatureCombAnalysis.isLightBulbOn Property

Parent Object: [CurvatureCombAnalysis](CurvatureCombAnalysis.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/CurvatureCombAnalysis.h>

## Description

A property that gets and sets if the display is enabled for this Analysis object. If false, this analysis will be hidden. If true and the IsLightBulbOn property of the Analyses object is True the Analysis will be visible.

## Syntax

* [Python](#Python)
* [C++](#C++)

"curvatureCombAnalysis\_var" is a variable referencing a CurvatureCombAnalysis object. |

"curvatureCombAnalysis\_var" is a variable referencing a CurvatureCombAnalysis object. ```` ``` #include <Fusion/Fusion/CurvatureCombAnalysis.h>  // Get the value of the property. boolean propertyValue = curvatureCombAnalysis_var->isLightBulbOn();  // Set the value of the property, where value_var is a boolean. bool returnValue = curvatureCombAnalysis_var->isLightBulbOn(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version January 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
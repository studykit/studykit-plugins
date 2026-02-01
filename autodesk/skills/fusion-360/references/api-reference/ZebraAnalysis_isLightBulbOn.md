# ZebraAnalysis.isLightBulbOn Property

Parent Object: [ZebraAnalysis](ZebraAnalysis.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/ZebraAnalysis.h>

## Description

A property that gets and sets if the display is enabled for this Analysis object. If false, this analysis will be hidden. If true and the IsLightBulbOn property of the Analyses object is True the Analysis will be visible.

## Syntax

* [Python](#Python)
* [C++](#C++)

"zebraAnalysis\_var" is a variable referencing a ZebraAnalysis object. |

"zebraAnalysis\_var" is a variable referencing a ZebraAnalysis object. ```` ``` #include <Fusion/Fusion/ZebraAnalysis.h>  // Get the value of the property. boolean propertyValue = zebraAnalysis_var->isLightBulbOn();  // Set the value of the property, where value_var is a boolean. bool returnValue = zebraAnalysis_var->isLightBulbOn(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version January 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
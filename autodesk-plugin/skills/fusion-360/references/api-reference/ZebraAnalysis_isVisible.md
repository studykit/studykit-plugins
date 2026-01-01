# ZebraAnalysis.isVisible Property

Parent Object: [ZebraAnalysis](ZebraAnalysis.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/ZebraAnalysis.h>

## Description

Gets if this Analysis is currently visible in the graphics window. The visibility is controlled by a combination of the isLightBulbOn properties of the Analyses collection object and the Analysis object. If both are true, the Analysis will be visible.

## Syntax

* [Python](#Python)
* [C++](#C++)

"zebraAnalysis\_var" is a variable referencing a ZebraAnalysis object. |

"zebraAnalysis\_var" is a variable referencing a ZebraAnalysis object. ```` ``` #include <Fusion/Fusion/ZebraAnalysis.h>  // Get the value of the property. boolean propertyValue = zebraAnalysis_var->isVisible(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version January 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
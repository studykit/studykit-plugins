# ZebraAnalysis.entityToken Property

Parent Object: [ZebraAnalysis](ZebraAnalysis.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/ZebraAnalysis.h>

## Description

Returns a token for the Analysis object. The token can be saved and used later with the Design.findEntityByToken method to get back the same Analysis.

## Syntax

* [Python](#Python)
* [C++](#C++)

"zebraAnalysis\_var" is a variable referencing a ZebraAnalysis object.  ```` ``` # Get the value of the property. propertyValue = zebraAnalysis_var.entityToken ``` ```` |

"zebraAnalysis\_var" is a variable referencing a ZebraAnalysis object. ```` ``` #include <Fusion/Fusion/ZebraAnalysis.h>  // Get the value of the property. string propertyValue = zebraAnalysis_var->entityToken(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
# MinimumRadiusAnalysis.entityToken Property

Parent Object: [MinimumRadiusAnalysis](MinimumRadiusAnalysis.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/MinimumRadiusAnalysis.h>

## Description

Returns a token for the Analysis object. The token can be saved and used later with the Design.findEntityByToken method to get back the same Analysis.

## Syntax

* [Python](#Python)
* [C++](#C++)

"minimumRadiusAnalysis\_var" is a variable referencing a MinimumRadiusAnalysis object.  ```` ``` # Get the value of the property. propertyValue = minimumRadiusAnalysis_var.entityToken ``` ```` |

"minimumRadiusAnalysis\_var" is a variable referencing a MinimumRadiusAnalysis object. ```` ``` #include <Fusion/Fusion/MinimumRadiusAnalysis.h>  // Get the value of the property. string propertyValue = minimumRadiusAnalysis_var->entityToken(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
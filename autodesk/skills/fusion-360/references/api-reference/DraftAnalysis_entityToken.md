# DraftAnalysis.entityToken Property

Parent Object: [DraftAnalysis](DraftAnalysis.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/DraftAnalysis.h>

## Description

Returns a token for the Analysis object. The token can be saved and used later with the Design.findEntityByToken method to get back the same Analysis.

## Syntax

* [Python](#Python)
* [C++](#C++)

"draftAnalysis\_var" is a variable referencing a DraftAnalysis object.  ```` ``` # Get the value of the property. propertyValue = draftAnalysis_var.entityToken ``` ```` |

"draftAnalysis\_var" is a variable referencing a DraftAnalysis object. ```` ``` #include <Fusion/Fusion/DraftAnalysis.h>  // Get the value of the property. string propertyValue = draftAnalysis_var->entityToken(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
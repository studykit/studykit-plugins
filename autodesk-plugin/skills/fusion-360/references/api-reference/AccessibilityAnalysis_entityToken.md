# AccessibilityAnalysis.entityToken Property

Parent Object: [AccessibilityAnalysis](AccessibilityAnalysis.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/AccessibilityAnalysis.h>

## Description

Returns a token for the Analysis object. The token can be saved and used later with the Design.findEntityByToken method to get back the same Analysis.

## Syntax

* [Python](#Python)
* [C++](#C++)

"accessibilityAnalysis\_var" is a variable referencing an AccessibilityAnalysis object.  ```` ``` # Get the value of the property. propertyValue = accessibilityAnalysis_var.entityToken ``` ```` |

"accessibilityAnalysis\_var" is a variable referencing an AccessibilityAnalysis object. ```` ``` #include <Fusion/Fusion/AccessibilityAnalysis.h>  // Get the value of the property. string propertyValue = accessibilityAnalysis_var->entityToken(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
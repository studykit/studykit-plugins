# Analysis.entityToken Property

Parent Object: [Analysis](Analysis.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/Analysis.h>

## Description

Returns a token for the Analysis object. The token can be saved and used later with the Design.findEntityByToken method to get back the same Analysis.

## Syntax

* [Python](#Python)
* [C++](#C++)

"analysis\_var" is a variable referencing an Analysis object.  ```` ``` # Get the value of the property. propertyValue = analysis_var.entityToken ``` ```` |

"analysis\_var" is a variable referencing an Analysis object. ```` ``` #include <Fusion/Fusion/Analysis.h>  // Get the value of the property. string propertyValue = analysis_var->entityToken(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
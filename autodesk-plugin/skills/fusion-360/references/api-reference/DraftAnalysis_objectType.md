# DraftAnalysis.objectType Property

Parent Object: [DraftAnalysis](DraftAnalysis.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/DraftAnalysis.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"draftAnalysis\_var" is a variable referencing a DraftAnalysis object.  ```` ``` # Get the value of the property. propertyValue = draftAnalysis_var.objectType ``` ```` |

"draftAnalysis\_var" is a variable referencing a DraftAnalysis object. ```` ``` #include <Fusion/Fusion/DraftAnalysis.h>  // Get the value of the property. string propertyValue = draftAnalysis_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
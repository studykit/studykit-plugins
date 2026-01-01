# DraftAnalyses.objectType Property

Parent Object: [DraftAnalyses](DraftAnalyses.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/DraftAnalyses.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"draftAnalyses\_var" is a variable referencing a DraftAnalyses object.  ```` ``` # Get the value of the property. propertyValue = draftAnalyses_var.objectType ``` ```` |

"draftAnalyses\_var" is a variable referencing a DraftAnalyses object. ```` ``` #include <Fusion/Fusion/DraftAnalyses.h>  // Get the value of the property. string propertyValue = draftAnalyses_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
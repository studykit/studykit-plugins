# DraftAnalysis.isValid Property

Parent Object: [DraftAnalysis](DraftAnalysis.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/DraftAnalysis.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"draftAnalysis\_var" is a variable referencing a DraftAnalysis object. |

"draftAnalysis\_var" is a variable referencing a DraftAnalysis object. ```` ``` #include <Fusion/Fusion/DraftAnalysis.h>  // Get the value of the property. boolean propertyValue = draftAnalysis_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version January 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
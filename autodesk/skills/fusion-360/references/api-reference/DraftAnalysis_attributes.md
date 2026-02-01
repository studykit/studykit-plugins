# DraftAnalysis.attributes Property

Parent Object: [DraftAnalysis](DraftAnalysis.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/DraftAnalysis.h>

## Description

A property that returns the collection of attributes associated with this Analysis.

## Syntax

* [Python](#Python)
* [C++](#C++)

"draftAnalysis\_var" is a variable referencing a DraftAnalysis object. |

"draftAnalysis\_var" is a variable referencing a DraftAnalysis object. ```` ``` #include <Fusion/Fusion/DraftAnalysis.h>  // Get the value of the property. Ptr<Attributes> propertyValue = draftAnalysis_var->attributes(); ``` ```` |

## Property Value

This is a read only property whose value is an [Attributes](Attributes.htm).

## Version

Introduced in version January 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
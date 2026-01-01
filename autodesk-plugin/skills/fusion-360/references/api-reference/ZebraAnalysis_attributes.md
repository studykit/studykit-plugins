# ZebraAnalysis.attributes Property

Parent Object: [ZebraAnalysis](ZebraAnalysis.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/ZebraAnalysis.h>

## Description

A property that returns the collection of attributes associated with this Analysis.

## Syntax

* [Python](#Python)
* [C++](#C++)

"zebraAnalysis\_var" is a variable referencing a ZebraAnalysis object. |

"zebraAnalysis\_var" is a variable referencing a ZebraAnalysis object. ```` ``` #include <Fusion/Fusion/ZebraAnalysis.h>  // Get the value of the property. Ptr<Attributes> propertyValue = zebraAnalysis_var->attributes(); ``` ```` |

## Property Value

This is a read only property whose value is an [Attributes](Attributes.htm).

## Version

Introduced in version January 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
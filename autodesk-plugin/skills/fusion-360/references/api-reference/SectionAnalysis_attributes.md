# SectionAnalysis.attributes Property

Parent Object: [SectionAnalysis](SectionAnalysis.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/SectionAnalysis.h>

## Description

A property that returns the collection of attributes associated with this Analysis.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sectionAnalysis\_var" is a variable referencing a SectionAnalysis object. |

"sectionAnalysis\_var" is a variable referencing a SectionAnalysis object. ```` ``` #include <Fusion/Fusion/SectionAnalysis.h>  // Get the value of the property. Ptr<Attributes> propertyValue = sectionAnalysis_var->attributes(); ``` ```` |

## Property Value

This is a read only property whose value is an [Attributes](Attributes.htm).

## Version

Introduced in version January 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
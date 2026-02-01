# Analyses.sectionAnalyses Property

Parent Object: [Analyses](Analyses.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/Analyses.h>

## Description

Returns the SectionAnalyses object, which provides access to any existing SectionAnalysis objects in the design.

## Syntax

* [Python](#Python)
* [C++](#C++)

"analyses\_var" is a variable referencing an Analyses object. |

"analyses\_var" is a variable referencing an Analyses object. ```` ``` #include <Fusion/Fusion/Analyses.h>  // Get the value of the property. Ptr<SectionAnalyses> propertyValue = analyses_var->sectionAnalyses(); ``` ```` |

## Property Value

This is a read only property whose value is a [SectionAnalyses](SectionAnalyses.htm).

## Version

Introduced in version January 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
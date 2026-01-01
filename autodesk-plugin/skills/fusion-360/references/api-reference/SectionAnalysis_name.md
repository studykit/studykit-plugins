# SectionAnalysis.name Property

Parent Object: [SectionAnalysis](SectionAnalysis.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/SectionAnalysis.h>

## Description

A property that gets and sets the name of the analysis. If you use a name that is not unique, Fusion will automatically append a number to the name to make it unique.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sectionAnalysis\_var" is a variable referencing a SectionAnalysis object. |

"sectionAnalysis\_var" is a variable referencing a SectionAnalysis object. ```` ``` #include <Fusion/Fusion/SectionAnalysis.h>  // Get the value of the property. string propertyValue = sectionAnalysis_var->name();  // Set the value of the property, where value_var is a string. bool returnValue = sectionAnalysis_var->name(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version January 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
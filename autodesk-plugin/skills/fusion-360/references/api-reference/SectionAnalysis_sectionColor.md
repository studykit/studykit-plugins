# SectionAnalysis.sectionColor Property

Parent Object: [SectionAnalysis](SectionAnalysis.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/SectionAnalysis.h>

## Description

A property that gets and sets the color of the section. A value of null indicates the component color should be used. The opacity value of the color is ignored.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sectionAnalysis\_var" is a variable referencing a SectionAnalysis object. |

"sectionAnalysis\_var" is a variable referencing a SectionAnalysis object. ```` ``` #include <Fusion/Fusion/SectionAnalysis.h>  // Get the value of the property. Ptr<Color> propertyValue = sectionAnalysis_var->sectionColor();  // Set the value of the property, where value_var is a Color. bool returnValue = sectionAnalysis_var->sectionColor(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Color](Color.htm).

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
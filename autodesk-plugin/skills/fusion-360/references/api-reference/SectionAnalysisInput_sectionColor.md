# SectionAnalysisInput.sectionColor Property

Parent Object: [SectionAnalysisInput](SectionAnalysisInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/SectionAnalysisInput.h>

## Description

A property that gets and sets the color of the section. This property defaults to null, indicating that the component color should be used. The opacity value of the color is ignored.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sectionAnalysisInput\_var" is a variable referencing a SectionAnalysisInput object. |

"sectionAnalysisInput\_var" is a variable referencing a SectionAnalysisInput object. ```` ``` #include <Fusion/Fusion/SectionAnalysisInput.h>  // Get the value of the property. Ptr<Color> propertyValue = sectionAnalysisInput_var->sectionColor();  // Set the value of the property, where value_var is a Color. bool returnValue = sectionAnalysisInput_var->sectionColor(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Color](Color.htm).

## Version

Introduced in version January 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
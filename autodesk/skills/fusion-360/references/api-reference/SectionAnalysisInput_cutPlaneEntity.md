# SectionAnalysisInput.cutPlaneEntity Property

Parent Object: [SectionAnalysisInput](SectionAnalysisInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/SectionAnalysisInput.h>

## Description

A property that gets and sets the planar entity used to define the cut plane and can be either a planar BRepFace or a ConstructionPlane object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sectionAnalysisInput\_var" is a variable referencing a SectionAnalysisInput object. |

"sectionAnalysisInput\_var" is a variable referencing a SectionAnalysisInput object. ```` ``` #include <Fusion/Fusion/SectionAnalysisInput.h>  // Get the value of the property. Ptr<Base> propertyValue = sectionAnalysisInput_var->cutPlaneEntity();  // Set the value of the property, where value_var is a Base. bool returnValue = sectionAnalysisInput_var->cutPlaneEntity(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Base](Base.htm).

## Version

Introduced in version January 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
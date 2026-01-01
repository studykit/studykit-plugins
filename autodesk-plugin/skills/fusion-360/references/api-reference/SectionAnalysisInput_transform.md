# SectionAnalysisInput.transform Property

Parent Object: [SectionAnalysisInput](SectionAnalysisInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/SectionAnalysisInput.h>

## Description

The initial position of the section plane is defined by the specified cut plane entity. Any offsets or rotations are defined by a transformation matrix that is applied to the initial position. This property allows you to get and set the transformation matrix.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sectionAnalysisInput\_var" is a variable referencing a SectionAnalysisInput object. |

"sectionAnalysisInput\_var" is a variable referencing a SectionAnalysisInput object. ```` ``` #include <Fusion/Fusion/SectionAnalysisInput.h>  // Get the value of the property. Ptr<Matrix3D> propertyValue = sectionAnalysisInput_var->transform();  // Set the value of the property, where value_var is a Matrix3D. bool returnValue = sectionAnalysisInput_var->transform(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Matrix3D](Matrix3D.htm).

## Version

Introduced in version January 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
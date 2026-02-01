# SectionAnalysis.transform Property

Parent Object: [SectionAnalysis](SectionAnalysis.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/SectionAnalysis.h>

## Description

The initial position of the section plane is defined by the specified cut plane entity. Any offsets or rotations are defined by a transformation matrix that is applied to the initial position. This property allows you to get and set the transformation matrix.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sectionAnalysis\_var" is a variable referencing a SectionAnalysis object. |

"sectionAnalysis\_var" is a variable referencing a SectionAnalysis object. ```` ``` #include <Fusion/Fusion/SectionAnalysis.h>  // Get the value of the property. Ptr<Matrix3D> propertyValue = sectionAnalysis_var->transform();  // Set the value of the property, where value_var is a Matrix3D. bool returnValue = sectionAnalysis_var->transform(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Matrix3D](Matrix3D.htm).

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
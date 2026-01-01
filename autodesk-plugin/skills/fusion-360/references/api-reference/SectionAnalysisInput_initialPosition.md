# SectionAnalysisInput.initialPosition Property

Parent Object: [SectionAnalysisInput](SectionAnalysisInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/SectionAnalysisInput.h>

## Description

Returns the matrix that describes the initial position and orientation of the specified cut plane entity. Any additional offsets or rotations are defined by a transformation matrix that is applied to this initial position matrix. That matrix is obtained and set using the transform property.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sectionAnalysisInput\_var" is a variable referencing a SectionAnalysisInput object. |

"sectionAnalysisInput\_var" is a variable referencing a SectionAnalysisInput object. ```` ``` #include <Fusion/Fusion/SectionAnalysisInput.h>  // Get the value of the property. Ptr<Matrix3D> propertyValue = sectionAnalysisInput_var->initialPosition(); ``` ```` |

## Property Value

This is a read only property whose value is a [Matrix3D](Matrix3D.htm).

## Version

Introduced in version January 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
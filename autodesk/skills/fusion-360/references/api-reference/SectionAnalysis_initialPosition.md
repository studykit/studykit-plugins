# SectionAnalysis.initialPosition Property

Parent Object: [SectionAnalysis](SectionAnalysis.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/SectionAnalysis.h>

## Description

Returns the matrix that describes the initial position and orientation of the specified cut plane entity. Any additional offsets or rotations are defined by a transformation matrix that is applied to this initial position. That matrix can be obtained and set using the transform property.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sectionAnalysis\_var" is a variable referencing a SectionAnalysis object. |

"sectionAnalysis\_var" is a variable referencing a SectionAnalysis object. ```` ``` #include <Fusion/Fusion/SectionAnalysis.h>  // Get the value of the property. Ptr<Matrix3D> propertyValue = sectionAnalysis_var->initialPosition(); ``` ```` |

## Property Value

This is a read only property whose value is a [Matrix3D](Matrix3D.htm).

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
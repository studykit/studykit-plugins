# Occurrence.transform2 Property

Parent Object: [Occurrence](Occurrence.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/Occurrence.h>

## Description

Gets and sets the 3d matrix data that defines this occurrences orientation and position in its assembly context. This property replaces the transform property, which has been retired because there are cases where it returns the incorrect results.

## Syntax

* [Python](#Python)
* [C++](#C++)

"occurrence\_var" is a variable referencing an Occurrence object. |

"occurrence\_var" is a variable referencing an Occurrence object. ```` ``` #include <Fusion/Components/Occurrence.h>  // Get the value of the property. Ptr<Matrix3D> propertyValue = occurrence_var->transform2();  // Set the value of the property, where value_var is a Matrix3D. bool returnValue = occurrence_var->transform2(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Matrix3D](Matrix3D.htm).

## Version

Introduced in version January 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
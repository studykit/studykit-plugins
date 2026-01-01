# FaceContourSelection.isSelectingSamePlaneFaces Property

Parent Object: [FaceContourSelection](FaceContourSelection.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/GeometrySelections/FaceContourSelection.h>

## Description

Property to get and set if all planar faces lying in the same plane as the selected face should be automatically selected as well.

## Syntax

* [Python](#Python)
* [C++](#C++)

"faceContourSelection\_var" is a variable referencing a FaceContourSelection object. |

"faceContourSelection\_var" is a variable referencing a FaceContourSelection object. ```` ``` #include <Cam/GeometrySelections/FaceContourSelection.h>  // Get the value of the property. boolean propertyValue = faceContourSelection_var->isSelectingSamePlaneFaces();  // Set the value of the property, where value_var is a boolean. bool returnValue = faceContourSelection_var->isSelectingSamePlaneFaces(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
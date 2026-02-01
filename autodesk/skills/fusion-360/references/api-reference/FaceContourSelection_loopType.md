# FaceContourSelection.loopType Property

Parent Object: [FaceContourSelection](FaceContourSelection.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/GeometrySelections/FaceContourSelection.h>

## Description

Property to get and set the desired loop type. The default is AllLoops.

## Syntax

* [Python](#Python)
* [C++](#C++)

"faceContourSelection\_var" is a variable referencing a FaceContourSelection object. |

"faceContourSelection\_var" is a variable referencing a FaceContourSelection object. ```` ``` #include <Cam/GeometrySelections/FaceContourSelection.h>  // Get the value of the property. LoopTypes propertyValue = faceContourSelection_var->loopType();  // Set the value of the property, where value_var is a LoopTypes. bool returnValue = faceContourSelection_var->loopType(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [LoopTypes](LoopTypes.htm).

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
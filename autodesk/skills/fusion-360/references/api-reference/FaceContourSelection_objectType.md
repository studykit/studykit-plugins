# FaceContourSelection.objectType Property

Parent Object: [FaceContourSelection](FaceContourSelection.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/GeometrySelections/FaceContourSelection.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"faceContourSelection\_var" is a variable referencing a FaceContourSelection object.  ```` ``` # Get the value of the property. propertyValue = faceContourSelection_var.objectType ``` ```` |

"faceContourSelection\_var" is a variable referencing a FaceContourSelection object. ```` ``` #include <Cam/GeometrySelections/FaceContourSelection.h>  // Get the value of the property. string propertyValue = faceContourSelection_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
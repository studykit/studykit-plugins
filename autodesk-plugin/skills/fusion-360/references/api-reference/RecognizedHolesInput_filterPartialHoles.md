# RecognizedHolesInput.filterPartialHoles Property

Parent Object: [RecognizedHolesInput](RecognizedHolesInput.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/HoleRecognition/RecognizedHolesInput.h>

## Description

Partial holes will not be included in recognized holes when set to true. Holes that intersect edges are considered partial holes. If a hole has multiple segments, such as a counterbore hole, all the segments inside the hole must intersect an edge for the hole to be considered a partial hole.

## Syntax

* [Python](#Python)
* [C++](#C++)

"recognizedHolesInput\_var" is a variable referencing a RecognizedHolesInput object. |

"recognizedHolesInput\_var" is a variable referencing a RecognizedHolesInput object. ```` ``` #include <Cam/HoleRecognition/RecognizedHolesInput.h>  // Get the value of the property. boolean propertyValue = recognizedHolesInput_var->filterPartialHoles();  // Set the value of the property, where value_var is a boolean. bool returnValue = recognizedHolesInput_var->filterPartialHoles(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
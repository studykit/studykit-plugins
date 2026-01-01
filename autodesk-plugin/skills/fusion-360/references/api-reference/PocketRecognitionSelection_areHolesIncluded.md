# PocketRecognitionSelection.areHolesIncluded Property

Parent Object: [PocketRecognitionSelection](PocketRecognitionSelection.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/GeometrySelections/PocketRecognitionSelection.h>

## Description

Flag to interpret holes as pockets.

## Syntax

* [Python](#Python)
* [C++](#C++)

"pocketRecognitionSelection\_var" is a variable referencing a PocketRecognitionSelection object. |

"pocketRecognitionSelection\_var" is a variable referencing a PocketRecognitionSelection object. ```` ``` #include <Cam/GeometrySelections/PocketRecognitionSelection.h>  // Get the value of the property. boolean propertyValue = pocketRecognitionSelection_var->areHolesIncluded();  // Set the value of the property, where value_var is a boolean. bool returnValue = pocketRecognitionSelection_var->areHolesIncluded(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version July 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
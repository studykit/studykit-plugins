# PocketRecognitionSelection.minimumCornerRadius Property

Parent Object: [PocketRecognitionSelection](PocketRecognitionSelection.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/GeometrySelections/PocketRecognitionSelection.h>

## Description

The smallest corner radius that can appear in a pocket to machine.

## Syntax

* [Python](#Python)
* [C++](#C++)

"pocketRecognitionSelection\_var" is a variable referencing a PocketRecognitionSelection object. |

"pocketRecognitionSelection\_var" is a variable referencing a PocketRecognitionSelection object. ```` ``` #include <Cam/GeometrySelections/PocketRecognitionSelection.h>  // Get the value of the property. double propertyValue = pocketRecognitionSelection_var->minimumCornerRadius();  // Set the value of the property, where value_var is a double. bool returnValue = pocketRecognitionSelection_var->minimumCornerRadius(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version July 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
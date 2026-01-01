# PocketRecognitionSelection.objectType Property

Parent Object: [PocketRecognitionSelection](PocketRecognitionSelection.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/GeometrySelections/PocketRecognitionSelection.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"pocketRecognitionSelection\_var" is a variable referencing a PocketRecognitionSelection object.  ```` ``` # Get the value of the property. propertyValue = pocketRecognitionSelection_var.objectType ``` ```` |

"pocketRecognitionSelection\_var" is a variable referencing a PocketRecognitionSelection object. ```` ``` #include <Cam/GeometrySelections/PocketRecognitionSelection.h>  // Get the value of the property. string propertyValue = pocketRecognitionSelection_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version July 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
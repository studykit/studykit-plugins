# RecognizedHoleGroups.objectType Property

Parent Object: [RecognizedHoleGroups](RecognizedHoleGroups.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/HoleRecognition/RecognizedHoleGroups.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"recognizedHoleGroups\_var" is a variable referencing a RecognizedHoleGroups object.  ```` ``` # Get the value of the property. propertyValue = recognizedHoleGroups_var.objectType ``` ```` |

"recognizedHoleGroups\_var" is a variable referencing a RecognizedHoleGroups object. ```` ``` #include <Cam/HoleRecognition/RecognizedHoleGroups.h>  // Get the value of the property. string propertyValue = recognizedHoleGroups_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version May 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
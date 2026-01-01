# RecognizedHolesInput.objectType Property

Parent Object: [RecognizedHolesInput](RecognizedHolesInput.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/HoleRecognition/RecognizedHolesInput.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"recognizedHolesInput\_var" is a variable referencing a RecognizedHolesInput object.  ```` ``` # Get the value of the property. propertyValue = recognizedHolesInput_var.objectType ``` ```` |

"recognizedHolesInput\_var" is a variable referencing a RecognizedHolesInput object. ```` ``` #include <Cam/HoleRecognition/RecognizedHolesInput.h>  // Get the value of the property. string propertyValue = recognizedHolesInput_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
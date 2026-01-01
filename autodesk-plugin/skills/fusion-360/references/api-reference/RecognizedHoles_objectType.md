# RecognizedHoles.objectType Property

Parent Object: [RecognizedHoles](RecognizedHoles.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/HoleRecognition/RecognizedHoles.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"recognizedHoles\_var" is a variable referencing a RecognizedHoles object.  ```` ``` # Get the value of the property. propertyValue = recognizedHoles_var.objectType ``` ```` |

"recognizedHoles\_var" is a variable referencing a RecognizedHoles object. ```` ``` #include <Cam/HoleRecognition/RecognizedHoles.h>  // Get the value of the property. string propertyValue = recognizedHoles_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version May 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
# RecognizedHole.objectType Property

Parent Object: [RecognizedHole](RecognizedHole.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/HoleRecognition/RecognizedHole.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"recognizedHole\_var" is a variable referencing a RecognizedHole object.  ```` ``` # Get the value of the property. propertyValue = recognizedHole_var.objectType ``` ```` |

"recognizedHole\_var" is a variable referencing a RecognizedHole object. ```` ``` #include <Cam/HoleRecognition/RecognizedHole.h>  // Get the value of the property. string propertyValue = recognizedHole_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version May 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
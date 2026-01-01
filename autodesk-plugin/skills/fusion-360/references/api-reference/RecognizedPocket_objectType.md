# RecognizedPocket.objectType Property

Parent Object: [RecognizedPocket](RecognizedPocket.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/PocketRecognition/RecognizedPocket.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"recognizedPocket\_var" is a variable referencing a RecognizedPocket object.  ```` ``` # Get the value of the property. propertyValue = recognizedPocket_var.objectType ``` ```` |

"recognizedPocket\_var" is a variable referencing a RecognizedPocket object. ```` ``` #include <Cam/PocketRecognition/RecognizedPocket.h>  // Get the value of the property. string propertyValue = recognizedPocket_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version July 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
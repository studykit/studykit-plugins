# RecognizedPockets.objectType Property

Parent Object: [RecognizedPockets](RecognizedPockets.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/PocketRecognition/RecognizedPockets.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"recognizedPockets\_var" is a variable referencing a RecognizedPockets object.  ```` ``` # Get the value of the property. propertyValue = recognizedPockets_var.objectType ``` ```` |

"recognizedPockets\_var" is a variable referencing a RecognizedPockets object. ```` ``` #include <Cam/PocketRecognition/RecognizedPockets.h>  // Get the value of the property. string propertyValue = recognizedPockets_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version July 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
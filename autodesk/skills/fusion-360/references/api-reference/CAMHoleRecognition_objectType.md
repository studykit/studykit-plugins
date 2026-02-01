# CAMHoleRecognition.objectType Property

Parent Object: [CAMHoleRecognition](CAMHoleRecognition.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/CAMHoleRecognition.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAMHoleRecognition\_var" is a variable referencing a CAMHoleRecognition object.  ```` ``` # Get the value of the property. propertyValue = cAMHoleRecognition_var.objectType ``` ```` |

"cAMHoleRecognition\_var" is a variable referencing a CAMHoleRecognition object. ```` ``` #include <Cam/CAM/CAMHoleRecognition.h>  // Get the value of the property. string propertyValue = cAMHoleRecognition_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
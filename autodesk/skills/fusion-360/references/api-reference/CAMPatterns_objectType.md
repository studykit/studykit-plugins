# CAMPatterns.objectType Property

Parent Object: [CAMPatterns](CAMPatterns.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/CAMPatterns.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAMPatterns\_var" is a variable referencing a CAMPatterns object.  ```` ``` # Get the value of the property. propertyValue = cAMPatterns_var.objectType ``` ```` |

"cAMPatterns\_var" is a variable referencing a CAMPatterns object. ```` ``` #include <Cam/CAM/CAMPatterns.h>  // Get the value of the property. string propertyValue = cAMPatterns_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
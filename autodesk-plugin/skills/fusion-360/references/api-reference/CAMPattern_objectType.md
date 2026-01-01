# CAMPattern.objectType Property

Parent Object: [CAMPattern](CAMPattern.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/CAMPattern.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAMPattern\_var" is a variable referencing a CAMPattern object.  ```` ``` # Get the value of the property. propertyValue = cAMPattern_var.objectType ``` ```` |

"cAMPattern\_var" is a variable referencing a CAMPattern object. ```` ``` #include <Cam/CAM/CAMPattern.h>  // Get the value of the property. string propertyValue = cAMPattern_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
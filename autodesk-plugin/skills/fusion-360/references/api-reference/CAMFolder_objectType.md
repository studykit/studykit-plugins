# CAMFolder.objectType Property

Parent Object: [CAMFolder](CAMFolder.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/CAMFolder.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAMFolder\_var" is a variable referencing a CAMFolder object.  ```` ``` # Get the value of the property. propertyValue = cAMFolder_var.objectType ``` ```` |

"cAMFolder\_var" is a variable referencing a CAMFolder object. ```` ``` #include <Cam/CAM/CAMFolder.h>  // Get the value of the property. string propertyValue = cAMFolder_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
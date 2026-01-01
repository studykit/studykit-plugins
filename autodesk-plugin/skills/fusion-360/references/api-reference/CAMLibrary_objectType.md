# CAMLibrary.objectType Property

Parent Object: [CAMLibrary](CAMLibrary.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Global/CAMLibrary.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAMLibrary\_var" is a variable referencing a CAMLibrary object.  ```` ``` # Get the value of the property. propertyValue = cAMLibrary_var.objectType ``` ```` |

"cAMLibrary\_var" is a variable referencing a CAMLibrary object. ```` ``` #include <Cam/Global/CAMLibrary.h>  // Get the value of the property. string propertyValue = cAMLibrary_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
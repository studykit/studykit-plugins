# CAMParameters.objectType Property

Parent Object: [CAMParameters](CAMParameters.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Operations/CAMParameters.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAMParameters\_var" is a variable referencing a CAMParameters object.  ```` ``` # Get the value of the property. propertyValue = cAMParameters_var.objectType ``` ```` |

"cAMParameters\_var" is a variable referencing a CAMParameters object. ```` ``` #include <Cam/Operations/CAMParameters.h>  // Get the value of the property. string propertyValue = cAMParameters_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
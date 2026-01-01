# GeneratedData.objectType Property

Parent Object: [GeneratedData](GeneratedData.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/GeneratedData/GeneratedData.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"generatedData\_var" is a variable referencing a GeneratedData object.  ```` ``` # Get the value of the property. propertyValue = generatedData_var.objectType ``` ```` |

"generatedData\_var" is a variable referencing a GeneratedData object. ```` ``` #include <Cam/GeneratedData/GeneratedData.h>  // Get the value of the property. string propertyValue = generatedData_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version July 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
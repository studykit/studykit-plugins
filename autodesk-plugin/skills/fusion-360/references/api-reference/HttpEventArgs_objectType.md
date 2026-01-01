# HttpEventArgs.objectType Property

Parent Object: [HttpEventArgs](HttpEventArgs.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/HttpEventArgs.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"httpEventArgs\_var" is a variable referencing a HttpEventArgs object.  ```` ``` # Get the value of the property. propertyValue = httpEventArgs_var.objectType ``` ```` |

"httpEventArgs\_var" is a variable referencing a HttpEventArgs object. ```` ``` #include <Core/Application/HttpEventArgs.h>  // Get the value of the property. string propertyValue = httpEventArgs_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
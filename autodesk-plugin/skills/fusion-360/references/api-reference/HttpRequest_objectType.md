# HttpRequest.objectType Property

Parent Object: [HttpRequest](HttpRequest.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/HttpRequest.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"httpRequest\_var" is a variable referencing a HttpRequest object.  ```` ``` # Get the value of the property. propertyValue = httpRequest_var.objectType ``` ```` |

"httpRequest\_var" is a variable referencing a HttpRequest object. ```` ``` #include <Core/Application/HttpRequest.h>  // Get the value of the property. string propertyValue = httpRequest_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
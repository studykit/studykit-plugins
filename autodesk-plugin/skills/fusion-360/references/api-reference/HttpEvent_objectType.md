# HttpEvent.objectType Property

Parent Object: [HttpEvent](HttpEvent.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/HttpEvent.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"httpEvent\_var" is a variable referencing a HttpEvent object.  ```` ``` # Get the value of the property. propertyValue = httpEvent_var.objectType ``` ```` |

"httpEvent\_var" is a variable referencing a HttpEvent object. ```` ``` #include <Core/Application/HttpEvent.h>  // Get the value of the property. string propertyValue = httpEvent_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
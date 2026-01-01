# URL.objectType Property

Parent Object: [URL](URL.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/URL.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"uRL\_var" is a variable referencing a URL object.  ```` ``` # Get the value of the property. propertyValue = uRL_var.objectType ``` ```` |

"uRL\_var" is a variable referencing a URL object. ```` ``` #include <Core/Application/URL.h>  // Get the value of the property. string propertyValue = uRL_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
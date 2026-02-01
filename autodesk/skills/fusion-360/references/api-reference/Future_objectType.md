# Future.objectType Property

Parent Object: [Future](Future.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Future.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"future\_var" is a variable referencing a Future object.  ```` ``` # Get the value of the property. propertyValue = future_var.objectType ``` ```` |

"future\_var" is a variable referencing a Future object. ```` ``` #include <Core/Application/Future.h>  // Get the value of the property. string propertyValue = future_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
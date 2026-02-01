# Status.objectType Property

Parent Object: [Status](Status.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Status.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"status\_var" is a variable referencing a Status object.  ```` ``` # Get the value of the property. propertyValue = status_var.objectType ``` ```` |

"status\_var" is a variable referencing a Status object. ```` ``` #include <Core/Application/Status.h>  // Get the value of the property. string propertyValue = status_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version July 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
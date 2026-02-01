# StatusMessages.objectType Property

Parent Object: [StatusMessages](StatusMessages.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/StatusMessages.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"statusMessages\_var" is a variable referencing a StatusMessages object.  ```` ``` # Get the value of the property. propertyValue = statusMessages_var.objectType ``` ```` |

"statusMessages\_var" is a variable referencing a StatusMessages object. ```` ``` #include <Core/Application/StatusMessages.h>  // Get the value of the property. string propertyValue = statusMessages_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version July 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
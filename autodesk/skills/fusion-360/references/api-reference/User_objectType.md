# User.objectType Property

Parent Object: [User](User.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/User.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"user\_var" is a variable referencing a User object.  ```` ``` # Get the value of the property. propertyValue = user_var.objectType ``` ```` |

"user\_var" is a variable referencing a User object. ```` ``` #include <Core/Application/User.h>  // Get the value of the property. string propertyValue = user_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
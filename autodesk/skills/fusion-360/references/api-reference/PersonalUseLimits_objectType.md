# PersonalUseLimits.objectType Property

Parent Object: [PersonalUseLimits](PersonalUseLimits.htm)
Defined in namespace "adsk::core" and the header file is <Core/Dashboard/PersonalUseLimits.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"personalUseLimits\_var" is a variable referencing a PersonalUseLimits object.  ```` ``` # Get the value of the property. propertyValue = personalUseLimits_var.objectType ``` ```` |

"personalUseLimits\_var" is a variable referencing a PersonalUseLimits object. ```` ``` #include <Core/Dashboard/PersonalUseLimits.h>  // Get the value of the property. string propertyValue = personalUseLimits_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version May 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
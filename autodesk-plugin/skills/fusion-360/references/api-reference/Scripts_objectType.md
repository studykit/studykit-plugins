# Scripts.objectType Property

Parent Object: [Scripts](Scripts.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Scripts.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"scripts\_var" is a variable referencing a Scripts object.  ```` ``` # Get the value of the property. propertyValue = scripts_var.objectType ``` ```` |

"scripts\_var" is a variable referencing a Scripts object. ```` ``` #include <Core/Application/Scripts.h>  // Get the value of the property. string propertyValue = scripts_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version October 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
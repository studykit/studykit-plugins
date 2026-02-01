# Torus.objectType Property

Parent Object: [Torus](Torus.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Torus.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"torus\_var" is a variable referencing a Torus object.  ```` ``` # Get the value of the property. propertyValue = torus_var.objectType ``` ```` |

"torus\_var" is a variable referencing a Torus object. ```` ``` #include <Core/Geometry/Torus.h>  // Get the value of the property. string propertyValue = torus_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
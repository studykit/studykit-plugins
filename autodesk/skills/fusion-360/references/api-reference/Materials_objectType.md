# Materials.objectType Property

Parent Object: [Materials](Materials.htm)
Defined in namespace "adsk::core" and the header file is <Core/Materials/Materials.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"materials\_var" is a variable referencing a Materials object.  ```` ``` # Get the value of the property. propertyValue = materials_var.objectType ``` ```` |

"materials\_var" is a variable referencing a Materials object. ```` ``` #include <Core/Materials/Materials.h>  // Get the value of the property. string propertyValue = materials_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
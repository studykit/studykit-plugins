# Material.objectType Property

Parent Object: [Material](Material.htm)
Defined in namespace "adsk::core" and the header file is <Core/Materials/Material.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"material\_var" is a variable referencing a Material object.  ```` ``` # Get the value of the property. propertyValue = material_var.objectType ``` ```` |

"material\_var" is a variable referencing a Material object. ```` ``` #include <Core/Materials/Material.h>  // Get the value of the property. string propertyValue = material_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
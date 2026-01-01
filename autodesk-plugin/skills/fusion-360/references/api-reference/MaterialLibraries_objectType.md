# MaterialLibraries.objectType Property

Parent Object: [MaterialLibraries](MaterialLibraries.htm)
Defined in namespace "adsk::core" and the header file is <Core/Materials/MaterialLibraries.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"materialLibraries\_var" is a variable referencing a MaterialLibraries object.  ```` ``` # Get the value of the property. propertyValue = materialLibraries_var.objectType ``` ```` |

"materialLibraries\_var" is a variable referencing a MaterialLibraries object. ```` ``` #include <Core/Materials/MaterialLibraries.h>  // Get the value of the property. string propertyValue = materialLibraries_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
# Surface.objectType Property

Parent Object: [Surface](Surface.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Surface.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"surface\_var" is a variable referencing a Surface object.  ```` ``` # Get the value of the property. propertyValue = surface_var.objectType ``` ```` |

"surface\_var" is a variable referencing a Surface object. ```` ``` #include <Core/Geometry/Surface.h>  // Get the value of the property. string propertyValue = surface_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
# NurbsSurface.objectType Property

Parent Object: [NurbsSurface](NurbsSurface.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/NurbsSurface.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"nurbsSurface\_var" is a variable referencing a NurbsSurface object.  ```` ``` # Get the value of the property. propertyValue = nurbsSurface_var.objectType ``` ```` |

"nurbsSurface\_var" is a variable referencing a NurbsSurface object. ```` ``` #include <Core/Geometry/NurbsSurface.h>  // Get the value of the property. string propertyValue = nurbsSurface_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
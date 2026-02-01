# BoundingBox3D.objectType Property

Parent Object: [BoundingBox3D](BoundingBox3D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/BoundingBox3D.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"boundingBox3D\_var" is a variable referencing a BoundingBox3D object.  ```` ``` # Get the value of the property. propertyValue = boundingBox3D_var.objectType ``` ```` |

"boundingBox3D\_var" is a variable referencing a BoundingBox3D object. ```` ``` #include <Core/Geometry/BoundingBox3D.h>  // Get the value of the property. string propertyValue = boundingBox3D_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
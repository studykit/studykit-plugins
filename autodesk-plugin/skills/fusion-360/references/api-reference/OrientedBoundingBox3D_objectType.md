# OrientedBoundingBox3D.objectType Property

Parent Object: [OrientedBoundingBox3D](OrientedBoundingBox3D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/OrientedBoundingBox3D.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"orientedBoundingBox3D\_var" is a variable referencing an OrientedBoundingBox3D object.  ```` ``` # Get the value of the property. propertyValue = orientedBoundingBox3D_var.objectType ``` ```` |

"orientedBoundingBox3D\_var" is a variable referencing an OrientedBoundingBox3D object. ```` ``` #include <Core/Geometry/OrientedBoundingBox3D.h>  // Get the value of the property. string propertyValue = orientedBoundingBox3D_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version December 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
# OrientedBoundingBox3D.isValid Property

Parent Object: [OrientedBoundingBox3D](OrientedBoundingBox3D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/OrientedBoundingBox3D.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"orientedBoundingBox3D\_var" is a variable referencing an OrientedBoundingBox3D object. |

"orientedBoundingBox3D\_var" is a variable referencing an OrientedBoundingBox3D object. ```` ``` #include <Core/Geometry/OrientedBoundingBox3D.h>  // Get the value of the property. boolean propertyValue = orientedBoundingBox3D_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version December 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
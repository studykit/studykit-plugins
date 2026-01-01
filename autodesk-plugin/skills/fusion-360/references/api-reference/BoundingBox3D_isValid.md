# BoundingBox3D.isValid Property

Parent Object: [BoundingBox3D](BoundingBox3D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/BoundingBox3D.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"boundingBox3D\_var" is a variable referencing a BoundingBox3D object. |

"boundingBox3D\_var" is a variable referencing a BoundingBox3D object. ```` ``` #include <Core/Geometry/BoundingBox3D.h>  // Get the value of the property. boolean propertyValue = boundingBox3D_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
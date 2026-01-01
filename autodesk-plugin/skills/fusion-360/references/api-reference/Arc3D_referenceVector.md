# Arc3D.referenceVector Property

Parent Object: [Arc3D](Arc3D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Arc3D.h>

## Description

Gets the reference vector of the arc.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arc3D\_var" is a variable referencing an Arc3D object. |

"arc3D\_var" is a variable referencing an Arc3D object. ```` ``` #include <Core/Geometry/Arc3D.h>  // Get the value of the property. Ptr<Vector3D> propertyValue = arc3D_var->referenceVector(); ``` ```` |

## Property Value

This is a read only property whose value is a [Vector3D](Vector3D.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
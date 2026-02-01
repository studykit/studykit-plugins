# Line3D.intersectWithSurface Method

Parent Object: [Line3D](Line3D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Line3D.h>

## Description

Intersect this line with a surface to get the intersection point(s).

## Syntax

* [Python](#Python)
* [C++](#C++)

"line3D\_var" is a variable referencing a [Line3D](Line3D.htm) object.```` ``` returnValue = line3D_var.intersectWithSurface(surface) ``` ```` |

"line3D\_var" is a variable referencing a [Line3D](Line3D.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ObjectCollection](ObjectCollection.htm) | Returns a collection of the intersection points. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| surface | [Surface](Surface.htm) | The intersecting surface. The surface can be a Plane, Cone, Cylinder, EllipticalCone, EllipticalCylinder, Sphere, Torus or a NurbsSurface. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
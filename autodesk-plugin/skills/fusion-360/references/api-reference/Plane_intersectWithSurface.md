# Plane.intersectWithSurface Method

Parent Object: [Plane](Plane.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Plane.h>

## Description

Intersect this plane with a surface to get the intersection point(s).

## Syntax

* [Python](#Python)
* [C++](#C++)

"plane\_var" is a variable referencing a [Plane](Plane.htm) object.```` ``` returnValue = plane_var.intersectWithSurface(surface) ``` ```` |

"plane\_var" is a variable referencing a [Plane](Plane.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ObjectCollection](ObjectCollection.htm) | Returns a collection of the intersection points. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| surface | [Surface](Surface.htm) | The intersecting surface. The surface can be a Plane, Cone, Cylinder, EllipticalCone, EllipticalCylinder, Sphere, Torus, or a NurbsSurface. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
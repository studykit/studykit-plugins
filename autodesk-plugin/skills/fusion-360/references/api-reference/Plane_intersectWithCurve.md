# Plane.intersectWithCurve Method

Parent Object: [Plane](Plane.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Plane.h>

## Description

Intersect this plane with a curve to get the intersection point(s).

## Syntax

* [Python](#Python)
* [C++](#C++)

"plane\_var" is a variable referencing a [Plane](Plane.htm) object.```` ``` returnValue = plane_var.intersectWithCurve(curve) ``` ```` |

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
| curve | [Curve3D](Curve3D.htm) | The intersecting curve. The curve can be a Line3D, InfininteLine3D, Circle3D, Arc3D, EllipticalArc3D, Ellipse3D, or NurbsCurve3D. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
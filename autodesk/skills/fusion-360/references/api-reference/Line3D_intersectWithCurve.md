# Line3D.intersectWithCurve Method

Parent Object: [Line3D](Line3D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Line3D.h>

## Description

Intersect this line with a curve to get the intersection point(s).

## Syntax

* [Python](#Python)
* [C++](#C++)

"line3D\_var" is a variable referencing a [Line3D](Line3D.htm) object.```` ``` returnValue = line3D_var.intersectWithCurve(curve) ``` ```` |

"line3D\_var" is a variable referencing a [Line3D](Line3D.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ObjectCollection](ObjectCollection.htm) | Returns a collection of the intersection points |

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
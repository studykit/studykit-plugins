# Plane.intersectWithPlane Method

Parent Object: [Plane](Plane.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Plane.h>

## Description

Creates an infinite line at the intersection of this plane with another plane.

## Syntax

* [Python](#Python)
* [C++](#C++)

"plane\_var" is a variable referencing a [Plane](Plane.htm) object.```` ``` returnValue = plane_var.intersectWithPlane(plane) ``` ```` |

"plane\_var" is a variable referencing a [Plane](Plane.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [InfiniteLine3D](InfiniteLine3D.htm) | Returns an InfiniteLine3D object or null if the planes do not intersect (are parallel). |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| plane | [Plane](Plane.htm) | The plane to intersect with. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
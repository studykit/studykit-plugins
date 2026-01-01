# Plane.intersectWithLine Method

Parent Object: [Plane](Plane.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Plane.h>

## Description

Creates a 3D point at the intersection of this plane and a line.

## Syntax

* [Python](#Python)
* [C++](#C++)

"plane\_var" is a variable referencing a [Plane](Plane.htm) object.```` ``` returnValue = plane_var.intersectWithLine(line) ``` ```` |

"plane\_var" is a variable referencing a [Plane](Plane.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Point3D](Point3D.htm) | Returns a Point3D object or null if the plane and line do not intersect (are parallel). |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| line | [InfiniteLine3D](InfiniteLine3D.htm) | The line to intersect with. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
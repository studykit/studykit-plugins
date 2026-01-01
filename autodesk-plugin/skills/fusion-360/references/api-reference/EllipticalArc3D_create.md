# EllipticalArc3D.create Method

Parent Object: [EllipticalArc3D](EllipticalArc3D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/EllipticalArc3D.h>

## Description

Creates a transient 3D elliptical arc.

## Syntax

* [Python](#Python)
* [C++](#C++)

This is a static method. |

This is a static method. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [EllipticalArc3D](EllipticalArc3D.htm) | Returns the newly created elliptical arc or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| center | [Point3D](Point3D.htm) | The center point of the elliptical arc. |
| normal | [Vector3D](Vector3D.htm) | The normal vector of the elliptical arc. |
| majorAxis | [Vector3D](Vector3D.htm) | The major axis of the elliptical arc. |
| majorRadius | double | The major radius of the of the elliptical arc. |
| minorRadius | double | The minor radius of the of the elliptical arc. |
| startAngle | double | The start angle of the elliptical arc in radians, where 0 is along the major axis. |
| endAngle | double | The end angle of the elliptical arc in radians, where 0 is along the major axis. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
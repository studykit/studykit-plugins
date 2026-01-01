# EllipticalCone.create Method

Parent Object: [EllipticalCone](EllipticalCone.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/EllipticalCone.h>

## Description

Creates a transient elliptical cone object.

## Syntax

* [Python](#Python)
* [C++](#C++)

This is a static method. |

This is a static method. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [EllipticalCone](EllipticalCone.htm) | Returns the new EllipticalCone object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| origin | [Point3D](Point3D.htm) | The origin point (center) of the base of the cone. |
| axis | [Vector3D](Vector3D.htm) | The center axis (along the length) of the cone that defines its normal direction. |
| majorAxisDirection | [Vector3D](Vector3D.htm) | The direction of the major axis of the ellipse that defines the cone. |
| majorRadius | double | The major radius of the ellipse that defines the cone. |
| minorRadius | double | The minor radius of the ellipse that defines the cone. |
| halfAngle | double | The taper half-angle of the cone. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
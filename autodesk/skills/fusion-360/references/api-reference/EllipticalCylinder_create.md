# EllipticalCylinder.create Method

Parent Object: [EllipticalCylinder](EllipticalCylinder.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/EllipticalCylinder.h>

## Description

Creates a transient 3D elliptical cylinder object.

## Syntax

* [Python](#Python)
* [C++](#C++)

This is a static method. |

This is a static method. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [EllipticalCylinder](EllipticalCylinder.htm) | Returns the new EllipticalCylinder object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| origin | [Point3D](Point3D.htm) | The origin point (center) of the base of the cylinder. |
| axis | [Vector3D](Vector3D.htm) | The center axis (along the length) of the cylinder that defines its normal direction. |
| majorAxis | [Vector3D](Vector3D.htm) | The direction of the major axis of the ellipse that defines the cylinder. |
| majorRadius | double | The major radius of the ellipse that defines the cylinder. |
| minorRadius | double | The minor radius of the ellipse that defines the cylinder. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
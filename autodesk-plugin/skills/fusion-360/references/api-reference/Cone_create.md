# Cone.create Method

Parent Object: [Cone](Cone.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Cone.h>

## Description

Creates a transient cone object.

## Syntax

* [Python](#Python)
* [C++](#C++)

This is a static method. |

This is a static method. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Cone](Cone.htm) | Returns the new Cone object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| origin | [Point3D](Point3D.htm) | The origin point (center) of the base of the cone. |
| axis | [Vector3D](Vector3D.htm) | The center axis (along the length) of the cone that defines its normal direction. |
| radius | double | The radius of the cone. |
| halfAngle | double | The taper half-angle of the cone. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
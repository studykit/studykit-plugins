# Plane.createUsingDirections Method

Parent Object: [Plane](Plane.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Plane.h>

## Description

Creates a transient plane object by specifying an origin along with U and V directions.

## Syntax

* [Python](#Python)
* [C++](#C++)

This is a static method. |

This is a static method. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Plane](Plane.htm) | Returns the new plane object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| origin | [Point3D](Point3D.htm) | The origin point of the plane. |
| uDirection | [Vector3D](Vector3D.htm) | The U direction for the plane. |
| vDirection | [Vector3D](Vector3D.htm) | The V direction for the plane. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
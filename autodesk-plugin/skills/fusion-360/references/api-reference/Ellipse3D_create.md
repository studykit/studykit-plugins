# Ellipse3D.create Method

Parent Object: [Ellipse3D](Ellipse3D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Ellipse3D.h>

## Description

Creates a transient 3D ellipse object.

## Syntax

* [Python](#Python)
* [C++](#C++)

This is a static method. |

This is a static method. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Ellipse3D](Ellipse3D.htm) | Returns the new Ellipse 3D object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| center | [Point3D](Point3D.htm) | The center point of the ellipse. |
| normal | [Vector3D](Vector3D.htm) | The normal vector of the ellipse. The plane through the center point and perpendicular to the normal vector defines the plane of the ellipse. |
| majorAxis | [Vector3D](Vector3D.htm) | The major axis of the ellipse |
| majorRadius | double | The major radius of the of the ellipse. |
| minorRadius | double | The minor radius of the of the ellipse. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
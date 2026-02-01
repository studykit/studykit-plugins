# Arc3D.createByCenter Method

Parent Object: [Arc3D](Arc3D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Arc3D.h>

## Description

Creates a transient 3D arc object by specifying a center point and radius.

## Syntax

* [Python](#Python)
* [C++](#C++)

This is a static method. |

This is a static method. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Arc3D](Arc3D.htm) | Returns the newly created arc or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| center | [Point3D](Point3D.htm) | The center point of the arc. |
| normal | [Vector3D](Vector3D.htm) | The normal vector of the arc. The plane perpendicular to this normal at the center point is the plane of the arc. |
| referenceVector | [Vector3D](Vector3D.htm) | A reference vector from which the start and end angles are measured from. This vector must be perpendicular to the normal vector. |
| radius | double | The radius of the arc. |
| startAngle | double | The start angle in radians. This angle is measured from the reference vector using the right hand rule around the normal vector. |
| endAngle | double | The end angle in radians. This angle is measured from the reference vector using the right hand rule around the normal vector. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
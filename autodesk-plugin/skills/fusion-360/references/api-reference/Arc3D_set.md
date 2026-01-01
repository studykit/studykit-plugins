# Arc3D.set Method

Parent Object: [Arc3D](Arc3D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Arc3D.h>

## Description

Sets all of the data defining the arc.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arc3D\_var" is a variable referencing an [Arc3D](Arc3D.htm) object.```` ``` returnValue = arc3D_var.set(center, normal, referenceVector, radius, startAngle, endAngle) ``` ```` |

"arc3D\_var" is a variable referencing an [Arc3D](Arc3D.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if successful |

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
# EllipticalArc3D.set Method

Parent Object: [EllipticalArc3D](EllipticalArc3D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/EllipticalArc3D.h>

## Description

Sets all of the data defining the elliptical arc.

## Syntax

* [Python](#Python)
* [C++](#C++)

"ellipticalArc3D\_var" is a variable referencing an [EllipticalArc3D](EllipticalArc3D.htm) object.```` ``` returnValue = ellipticalArc3D_var.set(center, normal, majorAxis, majorRadius, minorRadius, startAngle, endAngle) ``` ```` |

"ellipticalArc3D\_var" is a variable referencing an [EllipticalArc3D](EllipticalArc3D.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if successful. |

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
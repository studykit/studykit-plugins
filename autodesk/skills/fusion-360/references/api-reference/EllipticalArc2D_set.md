# EllipticalArc2D.set Method

Parent Object: [EllipticalArc2D](EllipticalArc2D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/EllipticalArc2D.h>

## Description

Sets all of the data defining the elliptical arc.

## Syntax

* [Python](#Python)
* [C++](#C++)

"ellipticalArc2D\_var" is a variable referencing an [EllipticalArc2D](EllipticalArc2D.htm) object.```` ``` returnValue = ellipticalArc2D_var.set(center, majorAxis, majorRadius, minorRadius, startAngle, endAngle) ``` ```` |

"ellipticalArc2D\_var" is a variable referencing an [EllipticalArc2D](EllipticalArc2D.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if redefining the elliptical arc is successful |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| center | [Point2D](Point2D.htm) | A Point2D object that defines the center of the elliptical arc. |
| majorAxis | [Vector2D](Vector2D.htm) | The major axis of the elliptical arc. |
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
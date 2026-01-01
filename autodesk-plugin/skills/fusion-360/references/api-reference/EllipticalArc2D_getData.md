# EllipticalArc2D.getData Method

Parent Object: [EllipticalArc2D](EllipticalArc2D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/EllipticalArc2D.h>

## Description

Gets all of the data defining the elliptical arc.

## Syntax

* [Python](#Python)
* [C++](#C++)

"ellipticalArc2D\_var" is a variable referencing an [EllipticalArc2D](EllipticalArc2D.htm) object. |

```` ```  #include <Core/Geometry/EllipticalArc2D.h ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if successful |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| center | [Point2D](Point2D.htm) | The output center point of the elliptical arc. |
| majorAxis | [Vector2D](Vector2D.htm) | The output major axis of the elliptical arc. |
| majorRadius | double | The output major radius of the of the elliptical arc. |
| minorRadius | double | The output minor radius of the of the elliptical arc. |
| startAngle | double | The output start angle of the elliptical arc in radians, where 0 is along the major axis. |
| endAngle | double | The output end angle of the elliptical arc in radians, where 0 is along the major axis. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
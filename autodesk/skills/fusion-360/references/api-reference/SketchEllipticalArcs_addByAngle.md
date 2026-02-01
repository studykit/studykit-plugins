# SketchEllipticalArcs.addByAngle Method

Parent Object: [SketchEllipticalArcs](SketchEllipticalArcs.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchEllipticalArcs.h>

## Description

Creates an elliptical sketch arc where the sweep of the arc is defined by the start and sweep angles.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchEllipticalArcs\_var" is a variable referencing a [SketchEllipticalArcs](SketchEllipticalArcs.htm) object.```` ``` returnValue = sketchEllipticalArcs_var.addByAngle(centerPoint, majorAxis, minorAxis, startAngle, sweepAngle) ``` ```` |

"sketchEllipticalArcs\_var" is a variable referencing a [SketchEllipticalArcs](SketchEllipticalArcs.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [SketchEllipticalArc](SketchEllipticalArc.htm) | Returns the newly created SketchEllipticalArc or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| centerPoint | [Base](Base.htm) | The center point of the ellipse. This can be either an existing SketchPoint or a Point3D object. |
| majorAxis | [Vector3D](Vector3D.htm) | The direction of the major axis. The magnitude of this vector defines the major radius. |
| minorAxis | [Vector3D](Vector3D.htm) | The direction of the minor axis. The magnitude of this vector defines the minor radius. This vector should be perpendicular to the major axis. |
| startAngle | double | The start angle of the elliptical arc in radians, where 0 is along the major axis. |
| sweepAngle | double | The sweep angle of the elliptical arc in radians, where a positive value is counterclockwise. |

## Version

Introduced in version May 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
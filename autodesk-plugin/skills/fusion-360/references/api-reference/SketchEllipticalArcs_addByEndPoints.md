# SketchEllipticalArcs.addByEndPoints Method

Parent Object: [SketchEllipticalArcs](SketchEllipticalArcs.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchEllipticalArcs.h>

## Description

Creates an elliptical sketch arc where the sweep of the arc is defined by two points.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchEllipticalArcs\_var" is a variable referencing a [SketchEllipticalArcs](SketchEllipticalArcs.htm) object.```` ``` returnValue = sketchEllipticalArcs_var.addByEndPoints(centerPoint, majorAxis, minorAxis, startPoint, endPoint) ``` ```` |

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
| startPoint | [Base](Base.htm) | The start point of the elliptical arc. This can be either an existing SketchPoint or a Point3D object. The point should lie on the defined ellipse. |
| endPoint | [Base](Base.htm) | The end point of the elliptical arc. This can be either an existing SketchPoint or a Point3D object. The point should lie on the defined ellipse and the elliptical arc is defined by a counterclockwise sweep from the start point to the end point. |

## Version

Introduced in version May 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
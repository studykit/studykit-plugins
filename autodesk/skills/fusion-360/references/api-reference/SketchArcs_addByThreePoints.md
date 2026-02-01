# SketchArcs.addByThreePoints Method

Parent Object: [SketchArcs](SketchArcs.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchArcs.h>

## Description

Creates a sketch arc that passes through the three points.

## Remarks

Sketch arcs always exist in a counterclockwise direction. Even though you can provide three that define an arc that will have a clockwise direction, the result will still be a counterclockwise arc. This means if you query the created sketch arc, the start and end points may be opposite of what you expect.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchArcs\_var" is a variable referencing a [SketchArcs](SketchArcs.htm) object.```` ``` returnValue = sketchArcs_var.addByThreePoints(startPoint, point, endPoint) ``` ```` |

"sketchArcs\_var" is a variable referencing a [SketchArcs](SketchArcs.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [SketchArc](SketchArc.htm) | Returns the newly created SketchArc or null in the case of a failure. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| startPoint | [Base](Base.htm) | The start point of the arc. This can be either an existing SketchPoint or a Point3D object. |
| point | [Point3D](Point3D.htm) | A point along the arc. This is a Point3D object. |
| endPoint | [Base](Base.htm) | The end point of the arc. This can be either an existing SketchPoint or a Point3D object. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [GeometricConstraints.addCoincident](GeometricConstraints_addCoincident_Sample.htm) | Demonstrates the GeometricConstraints.addCoincident method. |
| [SketchArcs.addByThreePoints](SketchArcs_addByThreePoints_Sample.htm) | Demonstrates the SketchArcs.addByThreePoints method. |
| [SketchArcs.breakCurve](SketchArcs_breakCurve_Sample.htm) | Demonstrates the SketchArc.breakCurve method. |
| [SketchArcs.extend](SketchArcs_extend_Sample.htm) | Demonstrates the SketchArc.extend method. |
| [SketchArcs.split](SketchArcs_split_Sample.htm) | Demonstrates the SketchArc.split method. |
| [SketchArcs.trim](SketchArcs_trim_Sample.htm) | Demonstrates the SketchArc.trim method. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
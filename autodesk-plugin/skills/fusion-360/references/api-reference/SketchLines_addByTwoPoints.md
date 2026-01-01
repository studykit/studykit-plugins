# SketchLines.addByTwoPoints Method

Parent Object: [SketchLines](SketchLines.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchLines.h>

## Description

Creates a sketch line between the two input points. The input points can be either existing SketchPoints or Point3D objects. If a SketchPoint is used the new line will be based on that sketch point and update if the sketch point is modified.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchLines\_var" is a variable referencing a [SketchLines](SketchLines.htm) object.```` ``` returnValue = sketchLines_var.addByTwoPoints(startPoint, endPoint) ``` ```` |

"sketchLines\_var" is a variable referencing a [SketchLines](SketchLines.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [SketchLine](SketchLine.htm) | Returns the newly created SketchLine object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| startPoint | [Base](Base.htm) | The start point of the line. It can be a SketchPoint or Point3D object. |
| endPoint | [Base](Base.htm) | The end point of the line. It can be a SketchPoint or Point3D object. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [API Sample that demonstrates creating sketch lines in various ways.](CreateSketchLines_Sample.htm) | Demonstrates several ways to create sketch lines, including as the result of creating a rectangle. |
| [Simple Revolve Feature Sample](SimpleRevolveFeatureSample_Sample.htm) | Creates a new revolve feature, resulting in a new component. |
| [SketchArcs.addFillet](SketchArcs_addFillet_Sample.htm) | Demonstrates the SketchArcs.addFillet method. |
| [SketchCircles.addByThreeTangents](SketchCircles_addByThreeTangents_Sample.htm) | Demonstrates the SketchCircles.addByThreeTangets method. |
| [SketchCircles.addByTwoTangents](SketchCircles_addByTwoTangents_Sample.htm) | Demonstrates the SketchCircles.addByTwoTangets method. |
| [SketchLines.addAngleChamfer](SketchLines_addAngleChamfer_Sample.htm) | Demonstrates the SketchLines.addAngleChamfer method. |
| [SketchLines.addByTwoPoints](SketchLines_addByTwoPoints_Sample.htm) | Demonstrates the SketchLines.addByTwoPoints method. |
| [SketchLines.addDistanceChamfer](SketchLines_addDistanceChamfer_Sample.htm) | Demonstrates the SketchLines.addDistanceChamfer method. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
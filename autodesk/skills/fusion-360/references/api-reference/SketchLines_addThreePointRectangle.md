# SketchLines.addThreePointRectangle Method

Parent Object: [SketchLines](SketchLines.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchLines.h>

## Description

Creates four sketch lines representing a rectangle where the first two points are the base corners of the rectangle and the third point defines the height.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchLines\_var" is a variable referencing a [SketchLines](SketchLines.htm) object.```` ``` returnValue = sketchLines_var.addThreePointRectangle(pointOne, pointTwo, pointThree) ``` ```` |

"sketchLines\_var" is a variable referencing a [SketchLines](SketchLines.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [SketchLineList](SketchLineList.htm) | Returns the four new sketch lines or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| pointOne | [Base](Base.htm) | The first corner of the rectangle. It can be a SketchPoint or Point3D object. |
| pointTwo | [Base](Base.htm) | The first corner of the rectangle. It can be a SketchPoint or Point3D object. |
| pointThree | [Point3D](Point3D.htm) | The first corner of the rectangle. a Point3D object defining the height of the rectangle. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [API Sample that demonstrates creating sketch lines in various ways.](CreateSketchLines_Sample.htm) | Demonstrates several ways to create sketch lines, including as the result of creating a rectangle. |
| [SketchLines.addThreePointRectangle](SketchLines_addThreePointRectangle_Sample.htm) | Demonstrates the SketchLines.addThreePointRectangle method. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
# SketchCircles.addByTwoTangents Method

Parent Object: [SketchCircles](SketchCircles.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchCircles.h>

## Description

Creates a sketch circle that is tangent to the two input lines. The two lines must lie on the x-y plane of the sketch.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchCircles\_var" is a variable referencing a [SketchCircles](SketchCircles.htm) object.```` ``` returnValue = sketchCircles_var.addByTwoTangents(tangentOne, tangentTwo, radius, hintPoint) ``` ```` |

"sketchCircles\_var" is a variable referencing a [SketchCircles](SketchCircles.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [SketchCircle](SketchCircle.htm) | Returns the newly created SketchCircle object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| tangentOne | [SketchLine](SketchLine.htm) | The first line that the circle will be tangent to. The line must lie on the x-y plane of the sketch. |
| tangentTwo | [SketchLine](SketchLine.htm) | The second line that the circle will be tangent to. The line must lie on the x-y plane of the sketch and cannot be parallel to the first line. |
| radius | double | The radius of the circle in centimeters. |
| hintPoint | [Point3D](Point3D.htm) | A point that specifies which of the possible four solutions to use when creating the circle. If you consider the two input lines to be infinite they create four quadrants which results in four possible solutions for the creation of the circle. The hint point is a point anywhere within the quadrant where you want the circle created. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [SketchCircles.addByTwoTangents](SketchCircles_addByTwoTangents_Sample.htm) | Demonstrates the SketchCircles.addByTwoTangets method. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
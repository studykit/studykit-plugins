# SketchCircles.addByThreePoints Method

Parent Object: [SketchCircles](SketchCircles.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchCircles.h>

## Description

Creates a sketch circle that passes through the three points. The three points must lie on the x-y plane of the sketch.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchCircles\_var" is a variable referencing a [SketchCircles](SketchCircles.htm) object.```` ``` returnValue = sketchCircles_var.addByThreePoints(pointOne, pointTwo, pointThree) ``` ```` |

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
| pointOne | [Point3D](Point3D.htm) | The first point that the circle will pass through. The z component must be zero. |
| pointTwo | [Point3D](Point3D.htm) | The second point that the circle will pass through. The z component must be zero. |
| pointThree | [Point3D](Point3D.htm) | The third point that the circle will pass through. The z component must be zero. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [SketchCircles.addByThreePoints](SketchCircles_addByThreePoints_Sample.htm) | Demonstrates the SketchCircles.addByThreePoints method. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
# SketchLines.addDistanceChamfer Method

Parent Object: [SketchLines](SketchLines.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchLines.h>

## Description

Creates a chamfer between two sketch lines. In the case where the two input lines cross each other creating an "X" shape, this results in four quadrants where the chamfer can be placed. The point arguments are used to define which of the four quadrants the chamfer should be created in. The two points define which side of the two lines should be kept and the other end will be trimmed by the chamfer. The easiest way to use this is to use the end points of the lines on the side you want to keep. In the case where the lines don't intersect or connect at the end points, there is only one valid quadrant for the chamfer so the points are ignored.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchLines\_var" is a variable referencing a [SketchLines](SketchLines.htm) object.```` ``` returnValue = sketchLines_var.addDistanceChamfer(firstLine, firstLinePoint, secondLine, secondLinePoint, distanceOne, distanceTwo) ``` ```` |

"sketchLines\_var" is a variable referencing a [SketchLines](SketchLines.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [SketchLine](SketchLine.htm) | Returns the newly created SketchLine object that represents the chamfer or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| firstLine | [SketchLine](SketchLine.htm) | The first line you want to chamfer. |
| firstLinePoint | [Point3D](Point3D.htm) | A point on the first line that is on the side of the intersection with the second line that you want to keep. |
| secondLine | [SketchLine](SketchLine.htm) | The second line you want to chamfer. |
| secondLinePoint | [Point3D](Point3D.htm) | A point on the second line that is on the side of the intersection with the first line that you want to keep. |
| distanceOne | double | Defines the distance of the start point of the chamfer line from the intersection point of the two lines along the first line. The distance is defined in centimeters. |
| distanceTwo | double | Defines the distance of the start point of the chamfer line from the intersection point of the two lines along the second line. The distance is defined in centimeters. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Sketch Chamfer API Sample](SketchChamferSample_Sample.htm) | Demonstrates creating a new sketch point. |
| [SketchLines.addDistanceChamfer](SketchLines_addDistanceChamfer_Sample.htm) | Demonstrates the SketchLines.addDistanceChamfer method. |

## Version

Introduced in version March 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
# SketchLines.addEdgePolygon Method

Parent Object: [SketchLines](SketchLines.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchLines.h>

## Description

Creates a polygon where two points specify an edge of the polygon. By specifying an edge, the size and position of the polygon is also defined.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchLines\_var" is a variable referencing a [SketchLines](SketchLines.htm) object.```` ``` returnValue = sketchLines_var.addEdgePolygon(pointOne, pointTwo, isRight, edgeCount) ``` ```` |

"sketchLines\_var" is a variable referencing a [SketchLines](SketchLines.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [SketchLineList](SketchLineList.htm) | Returns a list of the sketch lines that were created to represent the polygon or null in the case of bad input. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| pointOne | [Base](Base.htm) | The first point of the edge. |
| pointTwo | [Base](Base.htm) | The second point of the edge. |
| isRight | boolean | After defining points one and two, a polygon can be created on either side of the line defined by the two points. This argument specifies which side of the line the polygon will be created on. If this is true, the polygon will be created to the right of the line from the perspective of looking from point one to point two. If false, it will be to the left of the line. |
| edgeCount | integer | The number of edges in the resulting polygon. |

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
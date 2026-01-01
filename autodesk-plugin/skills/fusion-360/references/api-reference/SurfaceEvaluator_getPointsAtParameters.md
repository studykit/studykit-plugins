# SurfaceEvaluator.getPointsAtParameters Method

Parent Object: [SurfaceEvaluator](SurfaceEvaluator.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/SurfaceEvaluator.h>

## Description

Get the points on the surface that correspond to evaluating a set of parameter positions on the surface.

## Syntax

* [Python](#Python)
* [C++](#C++)

"surfaceEvaluator\_var" is a variable referencing a [SurfaceEvaluator](SurfaceEvaluator.htm) object. |

```` ```  #include <Core/Geometry/SurfaceEvaluator.h ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the points were successfully returned. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| parameters | Point2D[] | The array of parameter positions to evaluate the surface position at. Each parameter position must be within the range of the parameter extents as verified by isParameterOnFace. |
| points | Point3D[] | The output array of points corresponding to evaluating the curve at that parameter position. The length of this array will be equal to the length of the parameters array specified. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
# SurfaceEvaluator.getCurvatures Method

Parent Object: [SurfaceEvaluator](SurfaceEvaluator.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/SurfaceEvaluator.h>

## Description

Get the curvature values at a number of parameter positions on the surface.

## Syntax

* [Python](#Python)
* [C++](#C++)

"surfaceEvaluator\_var" is a variable referencing a [SurfaceEvaluator](SurfaceEvaluator.htm) object. |

```` ```  #include <Core/Geometry/SurfaceEvaluator.h ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the curvatures were successfully returned. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| parameters | Point2D[] | The array of parameter positions to return curvature information at. Each parameter position must be with the range of the parameter extents as verified by isParameterOnFace. |
| maxTangents | Vector3D[] | The output array of directions of maximum curvature at each position on the surface. The length of this array will be the same as the length of the parameters array provided. |
| maxCurvatures | double[] | The output array of the magnitude of the maximum curvature at each position on the surface. The length of this array will be the same as the length of the parameters array provided. |
| minCurvatures | double[] | The output array of the magnitude of the minimum curvature at each position on the surface. The minimum curvature direction is perpendicular to the maximum curvature tangent directions. The length of this array will be the same as the length of the parameters array provided. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
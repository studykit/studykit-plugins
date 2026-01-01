# SurfaceEvaluator.getCurvature Method

Parent Object: [SurfaceEvaluator](SurfaceEvaluator.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/SurfaceEvaluator.h>

## Description

Get the curvature values at a parameter positions on the surface.

## Syntax

* [Python](#Python)
* [C++](#C++)

"surfaceEvaluator\_var" is a variable referencing a [SurfaceEvaluator](SurfaceEvaluator.htm) object. |

```` ```  #include <Core/Geometry/SurfaceEvaluator.h ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the curvature was successfully returned. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| parameter | [Point2D](Point2D.htm) | The parameter positions to return curvature information at. |
| maxTangent | [Vector3D](Vector3D.htm) | The output directions of maximum curvature at the position on the surface. |
| maxCurvature | double | The output magnitude of the maximum curvature at the position on the surface. |
| minCurvature | double | The output magnitude of the minimum curvature at the position on the surface. The minimum curvature direction is perpendicular to the maximum curvature tangent directions. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
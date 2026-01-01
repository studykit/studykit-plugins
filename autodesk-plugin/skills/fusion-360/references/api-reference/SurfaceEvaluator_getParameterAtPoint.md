# SurfaceEvaluator.getParameterAtPoint Method

Parent Object: [SurfaceEvaluator](SurfaceEvaluator.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/SurfaceEvaluator.h>

## Description

Get the parameter position that correspond to a point on the surface. For reliable results, the point should lie on the surface within model tolerance. If the point does not lie on the surface, the parameter of the nearest point on the surface will generally be returned.

## Syntax

* [Python](#Python)
* [C++](#C++)

"surfaceEvaluator\_var" is a variable referencing a [SurfaceEvaluator](SurfaceEvaluator.htm) object. |

```` ```  #include <Core/Geometry/SurfaceEvaluator.h ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true of the parameter was successfully returned. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| point | [Point3D](Point3D.htm) | The point to get the curve parameter value at. |
| parameter | [Point2D](Point2D.htm) | The output parameter position corresponding to the point. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
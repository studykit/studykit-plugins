# SurfaceEvaluator.getModelCurveFromParametricCurve Method

Parent Object: [SurfaceEvaluator](SurfaceEvaluator.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/SurfaceEvaluator.h>

## Description

Creates the 3D equivalent curve in model space, of a 2D curve defined in the parametric space of the surface.

## Syntax

* [Python](#Python)
* [C++](#C++)

"surfaceEvaluator\_var" is a variable referencing a [SurfaceEvaluator](SurfaceEvaluator.htm) object.```` ``` returnValue = surfaceEvaluator_var.getModelCurveFromParametricCurve(parametricCurve) ``` ```` |

"surfaceEvaluator\_var" is a variable referencing a [SurfaceEvaluator](SurfaceEvaluator.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ObjectCollection](ObjectCollection.htm) | Returns an ObjectCollection containing one or more curves. When the SufaceEvaluatior is obtained from a face, and the curve cuts across internal boundaries of the face, multiple curves are returned. The returned curves are trimmed to the boundaries of the face. If the SurfaceEvaluator is obtained from a geometry object, a single curve returned because there are no boundaries with which to trim the curve. The type of curve(s) returned depends on the shape of the input curve and surface. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| parametricCurve | [Curve2D](Curve2D.htm) | The parameter space curve to map into this surface's parameter space. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
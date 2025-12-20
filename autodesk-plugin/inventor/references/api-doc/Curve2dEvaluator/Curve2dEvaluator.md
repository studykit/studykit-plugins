# Curve2dEvaluator Object

## Description

The Curve2dEvaluator object. See the article in the overviews section.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [GetCurvature](../Curve2dEvaluator/Curve2dEvaluator_GetCurvature.md) | Calculates the curvature direction and magnitude of the curve at the given parameter values. |
| [GetEndPoints](../Curve2dEvaluator/Curve2dEvaluator_GetEndPoints.md) | Gets the end points of the curve if the curve is bounded. |
| [GetFirstDerivatives](../Curve2dEvaluator/Curve2dEvaluator_GetFirstDerivatives.md) | Calculates the first order derivatives at the given parameter values on the curve. |
| [GetLengthAtParam](../Curve2dEvaluator/Curve2dEvaluator_GetLengthAtParam.md) | Calculate the length of the curve as measured between the specified parameter values. |
| [GetParamAnomaly](../Curve2dEvaluator/Curve2dEvaluator_GetParamAnomaly.md) | Gets general information about the parameterization of the curve, such as whether or not it is periodic, singular, or unbounded in the parameter domain. |
| [GetParamAtLength](../Curve2dEvaluator/Curve2dEvaluator_GetParamAtLength.md) | Calculates the parameter value at the point measured from the specified starting parameter along the curve. |
| [GetParamAtPoint](../Curve2dEvaluator/Curve2dEvaluator_GetParamAtPoint.md) | Calculates the parameter value on the curve that is equal to the specified point. The point must lie on the curve. |
| [GetParamExtents](../Curve2dEvaluator/Curve2dEvaluator_GetParamExtents.md) | Gets the valid parameter range of the curve if the curve is bounded. |
| [GetPointAtParam](../Curve2dEvaluator/Curve2dEvaluator_GetPointAtParam.md) | Calculates the coordinate points at the given parameter values on the curve. |
| [GetSecondDerivatives](../Curve2dEvaluator/Curve2dEvaluator_GetSecondDerivatives.md) | Calculates the second order derivatives at the given parameter values on the curve. |
| [GetStrokes](../Curve2dEvaluator/Curve2dEvaluator_GetStrokes.md) | Calculates a set of connected line segments that approximate the curve within the specified tolerance. |
| [GetTangent](../Curve2dEvaluator/Curve2dEvaluator_GetTangent.md) | Calculates the tangency directions at the given parameter values on the curve. |
| [GetThirdDerivatives](../Curve2dEvaluator/Curve2dEvaluator_GetThirdDerivatives.md) | Calculates the third order derivatives at the given parameter values on the curve. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Continuity](../Curve2dEvaluator/Curve2dEvaluator_Continuity.md) | Gets the level of continuity of the curve. The continuity is the largest order of continuity maintained for the entire curve. |
| [RangeBox](../Curve2dEvaluator/Curve2dEvaluator_RangeBox.md) | Property that returns a Box2D object which contains the lower-left and upper-right corners of a rectangle that is guaranteed to enclose this object. |

## Accessed From

[Arc2d.Evaluator](../Arc2d/Arc2d_Evaluator.md), [BSplineCurve2d.Evaluator](../BSplineCurve2d/BSplineCurve2d_Evaluator.md), [Circle2d.Evaluator](../Circle2d/Circle2d_Evaluator.md), [DrawingCurve.Evaluator2D](../DrawingCurve/DrawingCurve_Evaluator2D.md), [EdgeUse.Evaluator](../EdgeUse/EdgeUse_Evaluator.md), [EdgeUseProxy.Evaluator](../EdgeUseProxy/EdgeUseProxy_Evaluator.md), [EllipseFull2d.Evaluator](../EllipseFull2d/EllipseFull2d_Evaluator.md), [EllipticalArc2d.Evaluator](../EllipticalArc2d/EllipticalArc2d_Evaluator.md), [Line2d.Evaluator](../Line2d/Line2d_Evaluator.md), [LineSegment2d.Evaluator](../LineSegment2d/LineSegment2d_Evaluator.md), [Polyline2d.Evaluator](../Polyline2d/Polyline2d_Evaluator.md)

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
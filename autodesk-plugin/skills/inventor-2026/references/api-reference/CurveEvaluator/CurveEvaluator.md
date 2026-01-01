# CurveEvaluator Object

## Description

The CurveEvaluator object. See the article in the overviews section.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [GetCurvature](../CurveEvaluator/CurveEvaluator_GetCurvature.md) | Calculates the curvature direction and magnitude of the curve at the given parameter values. |
| [GetEndPoints](../CurveEvaluator/CurveEvaluator_GetEndPoints.md) | Gets the end points of the curve if the curve is bounded. |
| [GetFirstDerivatives](../CurveEvaluator/CurveEvaluator_GetFirstDerivatives.md) | Calculates the first order derivatives at the given parameter values on the curve. |
| [GetLengthAtParam](../CurveEvaluator/CurveEvaluator_GetLengthAtParam.md) | Calculate the length of the curve as measured between the specified parameter values. |
| [GetParamAnomaly](../CurveEvaluator/CurveEvaluator_GetParamAnomaly.md) | Gets general information about the parameterization of the curve, such as whether or not it is periodic, singular, or unbounded in the parameter domain. |
| [GetParamAtLength](../CurveEvaluator/CurveEvaluator_GetParamAtLength.md) | Calculates the parameter value at the point measured from the specified starting parameter along the curve. |
| [GetParamAtPoint](../CurveEvaluator/CurveEvaluator_GetParamAtPoint.md) | Calculates the parameter value on the curve that is equal to the specified point. The point must lie on the curve. |
| [GetParamExtents](../CurveEvaluator/CurveEvaluator_GetParamExtents.md) | Gets the valid parameter range of the curve if the curve is bounded. |
| [GetPointAtParam](../CurveEvaluator/CurveEvaluator_GetPointAtParam.md) | Calculates the coordinate points at the given parameter values on the curve. |
| [GetSecondDerivatives](../CurveEvaluator/CurveEvaluator_GetSecondDerivatives.md) | Calculates the second order derivatives at the given parameter values on the curve. |
| [GetStrokes](../CurveEvaluator/CurveEvaluator_GetStrokes.md) | Calculates a set of connected line segments that approximate the curve within the specified tolerance. |
| [GetTangent](../CurveEvaluator/CurveEvaluator_GetTangent.md) | Calculates the tangency directions at the given parameter values on the curve. |
| [GetThirdDerivatives](../CurveEvaluator/CurveEvaluator_GetThirdDerivatives.md) | Calculates the third order derivatives at the given parameter values on the curve. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Continuity](../CurveEvaluator/CurveEvaluator_Continuity.md) | Gets the level of continuity of the curve. The continuity is the largest order of continuity maintained for the entire curve. |
| [RangeBox](../CurveEvaluator/CurveEvaluator_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |

## Accessed From

[Arc3d.Evaluator](../Arc3d/Arc3d_Evaluator.md), [BSplineCurve.Evaluator](../BSplineCurve/BSplineCurve_Evaluator.md), [Circle.Evaluator](../Circle/Circle_Evaluator.md), [DrawingCurve.Evaluator3D](../DrawingCurve/DrawingCurve_Evaluator3D.md), [Edge.Evaluator](../Edge/Edge_Evaluator.md), [EdgeProxy.Evaluator](../EdgeProxy/EdgeProxy_Evaluator.md), [EllipseFull.Evaluator](../EllipseFull/EllipseFull_Evaluator.md), [EllipticalArc.Evaluator](../EllipticalArc/EllipticalArc_Evaluator.md), [Line.Evaluator](../Line/Line_Evaluator.md), [LineSegment.Evaluator](../LineSegment/LineSegment_Evaluator.md), [MeshEdge.Evaluator](../MeshEdge/MeshEdge_Evaluator.md), [MeshEdgeProxy.Evaluator](../MeshEdgeProxy/MeshEdgeProxy_Evaluator.md), [Polyline3d.Evaluator](../Polyline3d/Polyline3d_Evaluator.md), [PresentationEdge.Evaluator](../PresentationEdge/PresentationEdge_Evaluator.md), [PublicationEdge.Evaluator](PublicationEdge_Evaluator.md), [PublicationMeshEdge.Evaluator](PublicationMeshEdge_Evaluator.md)

## Version

Introduced in version 4

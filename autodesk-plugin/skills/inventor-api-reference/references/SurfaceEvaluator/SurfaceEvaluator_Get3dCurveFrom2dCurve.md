# SurfaceEvaluator.Get3dCurveFrom2dCurve Method

Parent Object: [SurfaceEvaluator](../SurfaceEvaluator/SurfaceEvaluator.md)

## Description

Function that calculates the equivalent 3D curve for a 2D curve defined in the parametric space of the surface associated with the evaluator. The resulting transient geometry 3D curve is returned. The type of curve(s) returned is dependent on the shape of the input curve and the surface.

## Syntax

SurfaceEvaluator.**Get3dCurveFrom2dCurve**( ***Curve2d*** As Object ) As Object

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Curve2d | Object | Input 2d transient geometry entity that defines geometry in the parametric space of the surface associated with the evaluator. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [3D Curve from Parametric Curve](../../sample-programs/ParameterCurveTo3D_Sample.md) | Demonstrates the conversion of a 2d parameteric space curve into the equivalent 3d model space curve. To use this sample you must have a part open. You can select any face and 3D curves will be drawn on the face using client graphics. |

## Version

Introduced in version 2013

# CurveEvaluator3D Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/Geometry/CurveEvaluator3D.h>

## Description

3D curve evaluator that is obtained from a transient curve and allows you to perform various evaluations on the curve.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](CurveEvaluator3D_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [getCurvature](CurveEvaluator3D_getCurvature.htm) | Get the curvature value at a parameter position on the curve. |
| [getCurvatures](CurveEvaluator3D_getCurvatures.htm) | Get the curvature values at a number of parameter positions on the curve. |
| [getEndPoints](CurveEvaluator3D_getEndPoints.htm) | Get the end points of the curve. |
| [getFirstDerivative](CurveEvaluator3D_getFirstDerivative.htm) | Get the first derivative of the curve at the specified parameter position. |
| [getFirstDerivatives](CurveEvaluator3D_getFirstDerivatives.htm) | Get the first derivatives of the curve at the specified parameter positions. |
| [getLengthAtParameter](CurveEvaluator3D_getLengthAtParameter.htm) | Get the length of the curve between two parameter positions on the curve. |
| [getParameterAtLength](CurveEvaluator3D_getParameterAtLength.htm) | Get the parameter position on the curve that is the specified curve length from the specified starting parameter position. |
| [getParameterAtPoint](CurveEvaluator3D_getParameterAtPoint.htm) | Get the parameter position that correspond to a point on the curve. For reliable results, the point should lie on the curve within model tolerance. If the point does not lie on the curve, the parameter of the nearest point on the curve will generally be returned. |
| [getParameterExtents](CurveEvaluator3D_getParameterExtents.htm) | Get the parametric range of the curve. |
| [getParametersAtPoints](CurveEvaluator3D_getParametersAtPoints.htm) | Get the parameter positions that correspond to a set of points on the curve. For reliable results, the points should lie on the curve within model tolerance. If the points do not lie on the curve, the parameter of the nearest point on the curve will generally be returned. |
| [getPointAtParameter](CurveEvaluator3D_getPointAtParameter.htm) | Get the point on the curve that corresponds to evaluating a parameter position on the curve. |
| [getPointsAtParameters](CurveEvaluator3D_getPointsAtParameters.htm) | Get the points on the curve that correspond to evaluating a set of parameter positions on the curve. |
| [getSecondDerivative](CurveEvaluator3D_getSecondDerivative.htm) | Get the second derivative of the curve at the specified parameter position. |
| [getSecondDerivatives](CurveEvaluator3D_getSecondDerivatives.htm) | Get the second derivatives of the curve at the specified parameter positions. |
| [getStrokes](CurveEvaluator3D_getStrokes.htm) | Get a sequence of points between two curve parameter positions. The points will be a linear interpolation along the curve between these two parameter positions where the maximum deviation between the curve and each line segment will not exceed the specified tolerance value. |
| [getTangent](CurveEvaluator3D_getTangent.htm) | Get the tangent to the curve at a parameter position on the curve. |
| [getTangents](CurveEvaluator3D_getTangents.htm) | Get the tangent to the curve at a number of parameter positions on the curve. |
| [getThirdDerivative](CurveEvaluator3D_getThirdDerivative.htm) | Get the third derivative of the curve at the specified parameter position. |
| [getThirdDerivatives](CurveEvaluator3D_getThirdDerivatives.htm) | Get the third derivatives of the curve at the specified parameter positions. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [isValid](CurveEvaluator3D_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](CurveEvaluator3D_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[Arc3D.evaluator](Arc3D_evaluator.htm), [BRepEdge.evaluator](BRepEdge_evaluator.htm), [Circle3D.evaluator](Circle3D_evaluator.htm), [Curve3D.evaluator](Curve3D_evaluator.htm), [Ellipse3D.evaluator](Ellipse3D_evaluator.htm), [EllipticalArc3D.evaluator](EllipticalArc3D_evaluator.htm), [InfiniteLine3D.evaluator](InfiniteLine3D_evaluator.htm), [Line3D.evaluator](Line3D_evaluator.htm), [NurbsCurve3D.evaluator](NurbsCurve3D_evaluator.htm), [Polyline3D.evaluator](Polyline3D_evaluator.htm), [SketchConicCurve.evaluator](SketchConicCurve_evaluator.htm), [SketchControlPointSpline.evaluator](SketchControlPointSpline_evaluator.htm), [SketchFixedSpline.evaluator](SketchFixedSpline_evaluator.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [SketchArcs.split](SketchArcs_split_Sample.htm) | Demonstrates the SketchArc.split method. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
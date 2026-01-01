# CurveEvaluator2D Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/Geometry/CurveEvaluator2D.h>

## Description

2D curve evaluator that is obtained from a transient curve and allows you to perform various evaluations on the curve.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](CurveEvaluator2D_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [getCurvature](CurveEvaluator2D_getCurvature.htm) | Get the curvature value at a parameter position on the curve. |
| [getCurvatures](CurveEvaluator2D_getCurvatures.htm) | Get the curvature values at a number of parameter positions on the curve. |
| [getEndPoints](CurveEvaluator2D_getEndPoints.htm) | Get the end points of the curve. |
| [getFirstDerivative](CurveEvaluator2D_getFirstDerivative.htm) | Get the first derivative of the curve at the specified parameter position. |
| [getFirstDerivatives](CurveEvaluator2D_getFirstDerivatives.htm) | Get the first derivatives of the curve at the specified parameter positions. |
| [getLengthAtParameter](CurveEvaluator2D_getLengthAtParameter.htm) | Get the length of the curve between two parameter positions on the curve. |
| [getParameterAtLength](CurveEvaluator2D_getParameterAtLength.htm) | Get the parameter position on the curve that is the specified curve length from the specified starting parameter position. |
| [getParameterAtPoint](CurveEvaluator2D_getParameterAtPoint.htm) | Get the parameter position that correspond to a point on the curve. For reliable results, the point should lie on the curve within model tolerance. If the point does not lie on the curve, the parameter of the nearest point on the curve will generally be returned. |
| [getParameterExtents](CurveEvaluator2D_getParameterExtents.htm) | Get the parametric range of the curve. |
| [getParametersAtPoints](CurveEvaluator2D_getParametersAtPoints.htm) | Get the parameter positions that correspond to a set of points on the curve. For reliable results, the points should lie on the curve within model tolerance. If the points do not lie on the curve, the parameter of the nearest point on the curve will generally be returned. |
| [getPointAtParameter](CurveEvaluator2D_getPointAtParameter.htm) | Get the point on the curve that corresponds to evaluating a parameter position on the curve. |
| [getPointsAtParameters](CurveEvaluator2D_getPointsAtParameters.htm) | Get the points on the curve that correspond to evaluating a set of parameter positions on the curve. |
| [getSecondDerivative](CurveEvaluator2D_getSecondDerivative.htm) | Get the second derivative of the curve at the specified parameter position. |
| [getSecondDerivatives](CurveEvaluator2D_getSecondDerivatives.htm) | Get the second derivatives of the curve at the specified parameter positions. |
| [getStrokes](CurveEvaluator2D_getStrokes.htm) | Get a sequence of points between two curve parameter positions. The points will be a linear interpolation along the curve between these two parameter positions where the maximum deviation between the curve and each line segment will not exceed the specified tolerance value. |
| [getTangent](CurveEvaluator2D_getTangent.htm) | Get the tangent to the curve at a parameter position on the curve. |
| [getTangents](CurveEvaluator2D_getTangents.htm) | Get the tangent to the curve at a number of parameter positions on the curve. |
| [getThirdDerivative](CurveEvaluator2D_getThirdDerivative.htm) | Get the third derivative of the curve at the specified parameter position. |
| [getThirdDerivatives](CurveEvaluator2D_getThirdDerivatives.htm) | Get the third derivatives of the curve at the specified parameter positions. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [isValid](CurveEvaluator2D_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](CurveEvaluator2D_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[Arc2D.evaluator](Arc2D_evaluator.htm), [BRepCoEdge.evaluator](BRepCoEdge_evaluator.htm), [Circle2D.evaluator](Circle2D_evaluator.htm), [Curve2D.evaluator](Curve2D_evaluator.htm), [Ellipse2D.evaluator](Ellipse2D_evaluator.htm), [EllipticalArc2D.evaluator](EllipticalArc2D_evaluator.htm), [Line2D.evaluator](Line2D_evaluator.htm), [NurbsCurve2D.evaluator](NurbsCurve2D_evaluator.htm), [Polyline2D.evaluator](Polyline2D_evaluator.htm)

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
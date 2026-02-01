# NurbsCurve2D.set Method

Parent Object: [NurbsCurve2D](NurbsCurve2D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/NurbsCurve2D.h>

## Description

Sets the data that defines a transient 2D NURBS rational b-spline object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"nurbsCurve2D\_var" is a variable referencing a [NurbsCurve2D](NurbsCurve2D.htm) object.```` ``` returnValue = nurbsCurve2D_var.set(controlPoints, degree, knots, isRational, weights, isPeriodic) ``` ```` |

"nurbsCurve2D\_var" is a variable referencing a [NurbsCurve2D](NurbsCurve2D.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if successful |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| controlPoints | Point2D[] | The array of control point that define the path of the spline |
| degree | integer | The degree of curvature of the spline |
| knots | double[] | An array of numbers that define the knots of the spline. |
| isRational | boolean | A bool indicating if the spline is rational. A rational spline must have a weight value for each control point. |
| weights | double[] | An array of numbers that define the weights for the spline. |
| isPeriodic | boolean | A bool specifying if the spline is to be Periodic. A periodic curve has a start point and end point that meet (with curvature continuity) forming a closed loop. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
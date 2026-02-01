# NurbsCurve3D.set Method

Parent Object: [NurbsCurve3D](NurbsCurve3D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/NurbsCurve3D.h>

## Description

Sets the data that defines a transient 3D NURBS rational b-spline object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"nurbsCurve3D\_var" is a variable referencing a [NurbsCurve3D](NurbsCurve3D.htm) object.```` ``` returnValue = nurbsCurve3D_var.set(controlPoints, degree, knots, isRational, weights, isPeriodic) ``` ```` |

"nurbsCurve3D\_var" is a variable referencing a [NurbsCurve3D](NurbsCurve3D.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| controlPoints | Point3D[] | The array of control point that define the path of the spline. |
| degree | integer | The degree of curvature of the spline. |
| knots | double[] | An array of numbers that define the knot vector of the spline. |
| isRational | boolean | A bool value indicating if the spline is rational. A rational spline must have a weight value for each control point. |
| weights | double[] | An array of numbers that define the weights for the spline. |
| isPeriodic | boolean | A bool indicating if the spline is Periodic. A periodic curve has a start point and end point that meet (with curvature continuity) forming a closed loop. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
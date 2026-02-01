# NurbsCurve3D.knots Property

Parent Object: [NurbsCurve3D](NurbsCurve3D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/NurbsCurve3D.h>

## Description

Returns an array of numbers that define the knot vector of the curve.

## Syntax

* [Python](#Python)
* [C++](#C++)

"nurbsCurve3D\_var" is a variable referencing a NurbsCurve3D object. |

"nurbsCurve3D\_var" is a variable referencing a NurbsCurve3D object. ```` ``` #include <Core/Geometry/NurbsCurve3D.h>  // Get the value of the property. std::vector<double> propertyValue = nurbsCurve3D_var->knots(); ``` ```` |

## Property Value

This is a read only property whose value is an array of type double.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
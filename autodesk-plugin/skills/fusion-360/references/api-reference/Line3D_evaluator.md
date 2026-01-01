# Line3D.evaluator Property

Parent Object: [Line3D](Line3D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Line3D.h>

## Description

Returns an evaluator object that lets you perform additional evaluations on the curve.

## Syntax

* [Python](#Python)
* [C++](#C++)

"line3D\_var" is a variable referencing a Line3D object. |

"line3D\_var" is a variable referencing a Line3D object. ```` ``` #include <Core/Geometry/Line3D.h>  // Get the value of the property. Ptr<CurveEvaluator3D> propertyValue = line3D_var->evaluator(); ``` ```` |

## Property Value

This is a read only property whose value is a [CurveEvaluator3D](CurveEvaluator3D.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
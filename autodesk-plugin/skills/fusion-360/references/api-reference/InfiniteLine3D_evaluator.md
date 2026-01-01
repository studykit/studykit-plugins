# InfiniteLine3D.evaluator Property

Parent Object: [InfiniteLine3D](InfiniteLine3D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/InfiniteLine3D.h>

## Description

Returns an evaluator object that lets you perform additional evaluations on the curve.

## Syntax

* [Python](#Python)
* [C++](#C++)

"infiniteLine3D\_var" is a variable referencing an InfiniteLine3D object. |

"infiniteLine3D\_var" is a variable referencing an InfiniteLine3D object. ```` ``` #include <Core/Geometry/InfiniteLine3D.h>  // Get the value of the property. Ptr<CurveEvaluator3D> propertyValue = infiniteLine3D_var->evaluator(); ``` ```` |

## Property Value

This is a read only property whose value is a [CurveEvaluator3D](CurveEvaluator3D.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
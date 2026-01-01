# CurveEvaluator3D.isValid Property

Parent Object: [CurveEvaluator3D](CurveEvaluator3D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/CurveEvaluator3D.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"curveEvaluator3D\_var" is a variable referencing a CurveEvaluator3D object. |

"curveEvaluator3D\_var" is a variable referencing a CurveEvaluator3D object. ```` ``` #include <Core/Geometry/CurveEvaluator3D.h>  // Get the value of the property. boolean propertyValue = curveEvaluator3D_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
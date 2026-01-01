# CurveEvaluator3D.getParameterAtPoint Method

Parent Object: [CurveEvaluator3D](CurveEvaluator3D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/CurveEvaluator3D.h>

## Description

Get the parameter position that correspond to a point on the curve. For reliable results, the point should lie on the curve within model tolerance. If the point does not lie on the curve, the parameter of the nearest point on the curve will generally be returned.

## Syntax

* [Python](#Python)
* [C++](#C++)

"curveEvaluator3D\_var" is a variable referencing a [CurveEvaluator3D](CurveEvaluator3D.htm) object. |

```` ```  #include <Core/Geometry/CurveEvaluator3D.h ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true of the parameter was successfully returned. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| point | [Point3D](Point3D.htm) | The point to get the curve parameter value at. |
| parameter | double | The output parameter position corresponding to the point. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
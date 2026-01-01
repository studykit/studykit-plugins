# CurveEvaluator3D.getTangent Method

Parent Object: [CurveEvaluator3D](CurveEvaluator3D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/CurveEvaluator3D.h>

## Description

Get the tangent to the curve at a parameter position on the curve.

## Syntax

* [Python](#Python)
* [C++](#C++)

"curveEvaluator3D\_var" is a variable referencing a [CurveEvaluator3D](CurveEvaluator3D.htm) object. |

```` ```  #include <Core/Geometry/CurveEvaluator3D.h ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the tangent was successfully returned. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| parameter | double | The parameter position to return the tangent at. This value must be within the range of the parameter extents as provided by getParameterExtents. |
| tangent | [Vector3D](Vector3D.htm) | The output tangent vector at the curve position. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
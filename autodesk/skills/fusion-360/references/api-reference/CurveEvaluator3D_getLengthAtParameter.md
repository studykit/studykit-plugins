# CurveEvaluator3D.getLengthAtParameter Method

Parent Object: [CurveEvaluator3D](CurveEvaluator3D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/CurveEvaluator3D.h>

## Description

Get the length of the curve between two parameter positions on the curve.

## Syntax

* [Python](#Python)
* [C++](#C++)

"curveEvaluator3D\_var" is a variable referencing a [CurveEvaluator3D](CurveEvaluator3D.htm) object. |

```` ```  #include <Core/Geometry/CurveEvaluator3D.h ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the length was successfully returned. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| fromParameter | double | The parameter position to measure the curve length from. This value must be within the range of the parameter extents as provided by getParameterExtents. |
| toParameter | double | The parameter position to measure the curve length to. This value must be within the range of the parameter extents as provided by getParameterExtents. |
| length | double | The output curve length between the from and to parameter positions on the curve. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
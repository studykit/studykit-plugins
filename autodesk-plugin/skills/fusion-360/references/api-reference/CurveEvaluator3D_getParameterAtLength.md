# CurveEvaluator3D.getParameterAtLength Method

Parent Object: [CurveEvaluator3D](CurveEvaluator3D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/CurveEvaluator3D.h>

## Description

Get the parameter position on the curve that is the specified curve length from the specified starting parameter position.

## Syntax

* [Python](#Python)
* [C++](#C++)

"curveEvaluator3D\_var" is a variable referencing a [CurveEvaluator3D](CurveEvaluator3D.htm) object. |

```` ```  #include <Core/Geometry/CurveEvaluator3D.h ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the parameter was successfully returned. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| fromParameter | double | The parameter position to start measuring the curve length from. This value must be within the range of the parameter extents as provided by getParameterExtents. |
| length | double | The curve length to offset the from parameter by. A negative length value will offset in the negative parameter direction. |
| parameter | double | The output parameter value that is the specified curve length from the starting parameter position. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
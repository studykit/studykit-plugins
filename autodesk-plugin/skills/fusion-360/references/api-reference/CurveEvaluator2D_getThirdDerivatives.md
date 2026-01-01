# CurveEvaluator2D.getThirdDerivatives Method

Parent Object: [CurveEvaluator2D](CurveEvaluator2D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/CurveEvaluator2D.h>

## Description

Get the third derivatives of the curve at the specified parameter positions.

## Syntax

* [Python](#Python)
* [C++](#C++)

"curveEvaluator2D\_var" is a variable referencing a [CurveEvaluator2D](CurveEvaluator2D.htm) object. |

```` ```  #include <Core/Geometry/CurveEvaluator2D.h ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the third derivatives were successfully returned. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| parameters | double[] | The array of parameter positions to get the curve third derivative at. Each parameter value must be within the range of the parameter extents as provided by getParameterExtents. |
| thirdDerivatives | Vector2D[] | The output array of third derivative vectors at each parameter position specified. The length of this array is equal to the length of the parameters array specified. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
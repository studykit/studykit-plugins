# CurveEvaluator3D.getStrokes Method

Parent Object: [CurveEvaluator3D](CurveEvaluator3D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/CurveEvaluator3D.h>

## Description

Get a sequence of points between two curve parameter positions. The points will be a linear interpolation along the curve between these two parameter positions where the maximum deviation between the curve and each line segment will not exceed the specified tolerance value.

## Syntax

* [Python](#Python)
* [C++](#C++)

"curveEvaluator3D\_var" is a variable referencing a [CurveEvaluator3D](CurveEvaluator3D.htm) object. |

```` ```  #include <Core/Geometry/CurveEvaluator3D.h ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the interpolation points were successfully returned. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| fromParameter | double | The starting parameter position to interpolate points from. The parameter value must be within the range of the parameter extents as provided by getParameterExtents. |
| toParameter | double | The ending parameter position to interpolate points to. The parameter value must be within the range of the parameter extents as provided by getParameterExtents. |
| tolerance | double | The maximum distance tolerance between the curve and the linear interpolation. |
| vertexCoordinates | Point3D[] | The output array of linear interpolation points. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
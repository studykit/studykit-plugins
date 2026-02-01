# SurfaceEvaluator.getSecondDerivatives Method

Parent Object: [SurfaceEvaluator](SurfaceEvaluator.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/SurfaceEvaluator.h>

## Description

Get the second derivatives of the surface at the specified parameter positions.

## Syntax

* [Python](#Python)
* [C++](#C++)

"surfaceEvaluator\_var" is a variable referencing a [SurfaceEvaluator](SurfaceEvaluator.htm) object. |

```` ```  #include <Core/Geometry/SurfaceEvaluator.h ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the second derivatives were successfully returned. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| parameters | Point2D[] | The array of parameter positions to get the surface second derivative at. Each parameter position must be within the range of the parameter extents as verified by isParameterOnFace. |
| partialsUU | Vector3D[] | The output array of second derivative UU partial vectors at each parameter position specified. The length of this array is equal to the length of the parameters array specified. |
| partialsUV | Vector3D[] | The output array of second derivative UV mixed partial vectors at each parameter position specified. The length of this array is equal to the length of the parameters array specified. |
| partialsVV | Vector3D[] | The output array of second derivative VV partial vectors at each parameter position specified. The length of this array is equal to the length of the parameters array specified. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
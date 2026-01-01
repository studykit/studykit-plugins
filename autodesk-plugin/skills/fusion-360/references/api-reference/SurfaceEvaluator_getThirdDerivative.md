# SurfaceEvaluator.getThirdDerivative Method

Parent Object: [SurfaceEvaluator](SurfaceEvaluator.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/SurfaceEvaluator.h>

## Description

Get the third derivative of the surface at the specified parameter position.

## Syntax

* [Python](#Python)
* [C++](#C++)

"surfaceEvaluator\_var" is a variable referencing a [SurfaceEvaluator](SurfaceEvaluator.htm) object. |

```` ```  #include <Core/Geometry/SurfaceEvaluator.h ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the third derivative was successfully returned. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| parameter | [Point2D](Point2D.htm) | The parameter position to get the surface third derivative at. The parameter position must be within the range of the parameter extents as verified by isParameterOnFace. |
| partialUUU | [Vector3D](Vector3D.htm) | The output third derivative UUU partial vector at each parameter position specified. |
| partialVVV | [Vector3D](Vector3D.htm) | The output third derivative VVV partial vector at each parameter position specified. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
# SurfaceEvaluator.getIsoCurve Method

Parent Object: [SurfaceEvaluator](SurfaceEvaluator.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/SurfaceEvaluator.h>

## Description

Gets (by extraction) a curve that follows a constant u or v parameter along the surface. The curve will have the same properties as the surface in the direction of the extraction. For example, when a curve is extracted from the periodic direction of a surface, the extracted curve will also be periodic. The type of curve returned is dependent on the shape the surface.

## Syntax

* [Python](#Python)
* [C++](#C++)

"surfaceEvaluator\_var" is a variable referencing a [SurfaceEvaluator](SurfaceEvaluator.htm) object.```` ``` returnValue = surfaceEvaluator_var.getIsoCurve(parameter, isUDirection) ``` ```` |

"surfaceEvaluator\_var" is a variable referencing a [SurfaceEvaluator](SurfaceEvaluator.htm) object.  ```` ``` #include <Core/Geometry/SurfaceEvaluator.h>  returnValue = surfaceEvaluator_var->getIsoCurve(parameter, isUDirection); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ObjectCollection](ObjectCollection.htm) | Returns an ObjectCollection that contains one or more curves. Multiple curves are returned when the SurfaceEvaluator is obtained from a Face and the curve cuts across internal boundaries. The resulting curves are trimmed to the boundaries of the Face. When the SurfaceEvaluator is obtained from a geometry object, a single curve is returned because there are no boundaries to trim the curve. The type of curve(s) returned is dependent on the shape of the surface. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| parameter | double | The parameter at which to extract the curve |
| isUDirection | boolean | A bool that indicates whether to extract the curve from the U or V direction |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
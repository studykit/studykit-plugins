# SurfaceEvaluator.isParameterOnFace Method

Parent Object: [SurfaceEvaluator](SurfaceEvaluator.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/SurfaceEvaluator.h>

## Description

Determines if the specified parameter position lies within the surface. When the SurfaceEvaluator is obtained from a BRepFace object, this will respect the boundaries of the face and return true when point is on the visible portion of the surface. When obtained from surface geometry it returns true if the point is within the parametric range of surface.

## Syntax

* [Python](#Python)
* [C++](#C++)

"surfaceEvaluator\_var" is a variable referencing a [SurfaceEvaluator](SurfaceEvaluator.htm) object.```` ``` returnValue = surfaceEvaluator_var.isParameterOnFace(parameter) ``` ```` |

"surfaceEvaluator\_var" is a variable referencing a [SurfaceEvaluator](SurfaceEvaluator.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the parameter position lies within the surface. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| parameter | [Point2D](Point2D.htm) | The parameter position to test. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
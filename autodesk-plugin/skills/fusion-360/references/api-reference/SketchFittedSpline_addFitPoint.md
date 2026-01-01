# SketchFittedSpline.addFitPoint Method

Parent Object: [SketchFittedSpline](SketchFittedSpline.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchFittedSpline.h>

## Description

Creates a new fit point at the specified parameter value.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchFittedSpline\_var" is a variable referencing a [SketchFittedSpline](SketchFittedSpline.htm) object.```` ``` returnValue = sketchFittedSpline_var.addFitPoint(parameter) ``` ```` |

"sketchFittedSpline\_var" is a variable referencing a [SketchFittedSpline](SketchFittedSpline.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [SketchPoint](SketchPoint.htm) | Returns the newly created SketchPoint that acts as the fit point. Fails in the case where an invalid parameter is specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| parameter | double | The parameter value at the position along the curve where you want to add the new fit point. The CurveEvaluator3D object provides utilities that support going from a 3D coordinate to a parameter value on the curve. |

## Version

Introduced in version September 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
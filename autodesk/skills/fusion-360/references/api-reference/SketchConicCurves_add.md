# SketchConicCurves.add Method

Parent Object: [SketchConicCurves](SketchConicCurves.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchConicCurves.h>

## Description

Creates a new conic curve.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchConicCurves\_var" is a variable referencing a [SketchConicCurves](SketchConicCurves.htm) object.```` ``` returnValue = sketchConicCurves_var.add(startPoint, endPoint, apexPoint, rhoValue) ``` ```` |

"sketchConicCurves\_var" is a variable referencing a [SketchConicCurves](SketchConicCurves.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [SketchConicCurve](SketchConicCurve.htm) | Returns the new conic curve or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| startPoint | [Base](Base.htm) | The start point of the conic curve. This can be either an existing SketchPoint or a Point3D object. |
| endPoint | [Base](Base.htm) | The end point of the conic curve. This can be either an existing SketchPoint or a Point3D object. |
| apexPoint | [Base](Base.htm) | The apex point of the conic curve. This can be either an existing SketchPoint or a Point3D object. |
| rhoValue | double | Double that specifies the rho value for the conic. This value must be greater than zero and less than one. |

## Version

Introduced in version May 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
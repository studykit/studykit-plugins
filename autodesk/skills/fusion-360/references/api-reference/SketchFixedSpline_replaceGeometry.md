# SketchFixedSpline.replaceGeometry Method

Parent Object: [SketchFixedSpline](SketchFixedSpline.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchFixedSpline.h>

## Description

Replaces the underlying NURBS curve that defines the shape of the fixed curve. This can only be used if the isNative property of the SketchFixedSpline returns false.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchFixedSpline\_var" is a variable referencing a [SketchFixedSpline](SketchFixedSpline.htm) object.```` ``` returnValue = sketchFixedSpline_var.replaceGeometry(nurbsCurve) ``` ```` |

"sketchFixedSpline\_var" is a variable referencing a [SketchFixedSpline](SketchFixedSpline.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the replacement was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| nurbsCurve | [NurbsCurve3D](NurbsCurve3D.htm) | A NurbsCurve3D object that defines a valid NURBS curve and will be used to replace the existing geometry definition. |

## Version

Introduced in version December 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
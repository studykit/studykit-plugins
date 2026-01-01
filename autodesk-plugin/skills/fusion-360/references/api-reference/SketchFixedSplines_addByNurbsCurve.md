# SketchFixedSplines.addByNurbsCurve Method

Parent Object: [SketchFixedSplines](SketchFixedSplines.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchFixedSplines.h>

## Description

Creates a new fixed spline using the input NurbsCurve3D to define the shape. The resulting curve is not editable by the user but can be updated via the API using the replaceGeometry method on the SketchFixedSpline object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchFixedSplines\_var" is a variable referencing a [SketchFixedSplines](SketchFixedSplines.htm) object.```` ``` returnValue = sketchFixedSplines_var.addByNurbsCurve(nurbsCurve) ``` ```` |

"sketchFixedSplines\_var" is a variable referencing a [SketchFixedSplines](SketchFixedSplines.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [SketchFixedSpline](SketchFixedSpline.htm) | Returns the newly created SketchFixedSpline object if the creation was successful or null if it failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| nurbsCurve | [NurbsCurve3D](NurbsCurve3D.htm) | A NurbsCurve3D object that defines a valid NURBS curve. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [SketchFixedSplines.addByNurbsCurve](SketchFixedSplines_addByNurbsCurve_Sample.htm) | Demonstrates the SketchFixedSplines.addByNurbsCurve method. |

## Version

Introduced in version December 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
# SketchControlPointSplines.add Method

Parent Object: [SketchControlPointSplines](SketchControlPointSplines.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchControlPointSplines.h>

## Description

Creates a new control point spline.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchControlPointSplines\_var" is a variable referencing a [SketchControlPointSplines](SketchControlPointSplines.htm) object.```` ``` returnValue = sketchControlPointSplines_var.add(controlPoints, degree) ``` ```` |

"sketchControlPointSplines\_var" is a variable referencing a [SketchControlPointSplines](SketchControlPointSplines.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [SketchControlPointSpline](SketchControlPointSpline.htm) | Returns the newly created SketchControlPointSpline object if the creation was successful or null if it failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| controlPoints | Base[] | An array of points that define the control points of the curve's polygon. They can be any combination of existing SketchPoint or Point3D objects. |
| degree | [SplineDegrees](SplineDegrees.htm) | Specifies the degree of the spline. Only degree 3 and degree 5 can be specified while creating the spline. |

## Version

Introduced in version July 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
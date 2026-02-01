# SketchFittedSplines.add Method

Parent Object: [SketchFittedSplines](SketchFittedSplines.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchFittedSplines.h>

## Description

Creates a new fitted spline through the specified points.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchFittedSplines\_var" is a variable referencing a [SketchFittedSplines](SketchFittedSplines.htm) object.```` ``` returnValue = sketchFittedSplines_var.add(fitPoints) ``` ```` |

"sketchFittedSplines\_var" is a variable referencing a [SketchFittedSplines](SketchFittedSplines.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [SketchFittedSpline](SketchFittedSpline.htm) | Returns the newly created SketchFittedSpline object if the creation was successful or null if it failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| fitPoints | [ObjectCollection](ObjectCollection.htm) | A collection of points that the curve will fit through. They can be any combination of existing SketchPoint or Point3D objects. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [GeometricConstraints.addSmooth](GeometricConstraints_addSmooth_Sample.htm) | Demonstrate the GeometricConstraints.addSmooth method. |
| [SketchFittedSplines.add](SketchFittedSplines_add_Sample.htm) | Demonstrates the SketchFittedSplines.add method. |
| [Sketch spline through points creation and relative functions API Sample](SketchSplineThroughPoints_Sample.htm) | Create a sketch spline with points and use some operations for spline tangent handle & curvature handle. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
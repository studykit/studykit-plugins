# SketchPoints.add Method

Parent Object: [SketchPoints](SketchPoints.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchPoints.h>

## Description

Creates a point at the specified location. This is the equivalent of creating a sketch point using the Point command in the user interface and will create a visible point in the graphics window.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchPoints\_var" is a variable referencing a [SketchPoints](SketchPoints.htm) object.```` ``` returnValue = sketchPoints_var.add(point) ``` ```` |

"sketchPoints\_var" is a variable referencing a [SketchPoints](SketchPoints.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [SketchPoint](SketchPoint.htm) | Returns the new sketch point or null if the creation fails. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| point | [Point3D](Point3D.htm) | The coordinate location to create the sketch point. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [GeometricConstraint.addMidPont](GeometricConstraint_addMidPont_Sample.htm) | Demonstrate the GeometricConstraint.addMidPont method. |
| [GeometricConstraints.addCoincident](GeometricConstraints_addCoincident_Sample.htm) | Demonstrates the GeometricConstraints.addCoincident method. |
| [SketchPoint.add](SketchPoint_add_Sample.htm) | Demonstrates the SketchPoint.add method. |
| [Sketch Point API Sample](SketchPointSample_Sample.htm) | Demonstrates creating a new sketch point. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
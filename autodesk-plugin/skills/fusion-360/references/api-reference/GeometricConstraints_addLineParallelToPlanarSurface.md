# GeometricConstraints.addLineParallelToPlanarSurface Method

Parent Object: [GeometricConstraints](GeometricConstraints.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/GeometricConstraints.h>

## Description

Creates a new parallel constraint between a sketch line and a planar surface that will constrain the line to lie on a plane parallel to the specified surface.

## Syntax

* [Python](#Python)
* [C++](#C++)

"geometricConstraints\_var" is a variable referencing a [GeometricConstraints](GeometricConstraints.htm) object.```` ``` returnValue = geometricConstraints_var.addLineParallelToPlanarSurface(line, planarSurface) ``` ```` |

"geometricConstraints\_var" is a variable referencing a [GeometricConstraints](GeometricConstraints.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [LineParallelToPlanarSurfaceConstraint](LineParallelToPlanarSurfaceConstraint.htm) | Returns the newly created LineParallelToPlanarSurfaceConstraint object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| line | [SketchLine](SketchLine.htm) | The SketchLine to constrain to the surface. |
| planarSurface | [Base](Base.htm) | The planar BRepFace or CosntructionPlane the sketch line will be parallel to. |

## Version

Introduced in version September 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
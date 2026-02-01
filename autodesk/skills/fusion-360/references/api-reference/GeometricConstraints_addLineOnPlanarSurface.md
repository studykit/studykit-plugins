# GeometricConstraints.addLineOnPlanarSurface Method

Parent Object: [GeometricConstraints](GeometricConstraints.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/GeometricConstraints.h>

## Description

Creates a new constraint that forces the sketch line to lie on a planar surface.

## Syntax

* [Python](#Python)
* [C++](#C++)

"geometricConstraints\_var" is a variable referencing a [GeometricConstraints](GeometricConstraints.htm) object.```` ``` returnValue = geometricConstraints_var.addLineOnPlanarSurface(line, planarSurface) ``` ```` |

"geometricConstraints\_var" is a variable referencing a [GeometricConstraints](GeometricConstraints.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [LineOnPlanarSurfaceConstraint](LineOnPlanarSurfaceConstraint.htm) | Returns the newly created LineOnPlanarSurfaceConstraint object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| line | [SketchLine](SketchLine.htm) | The SketchLine to constrain to the surface. |
| planarSurface | [Base](Base.htm) | The planar BRepFace or CosntructionPlane the sketch line will lie on. |

## Version

Introduced in version September 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
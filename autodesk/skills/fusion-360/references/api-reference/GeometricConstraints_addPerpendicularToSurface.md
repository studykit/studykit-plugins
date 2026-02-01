# GeometricConstraints.addPerpendicularToSurface Method

Parent Object: [GeometricConstraints](GeometricConstraints.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/GeometricConstraints.h>

## Description

Creates a new perpendicular constraint that forces the sketch curve to be perpendicular to the specified surface. Line and spline curves are supported.

## Syntax

* [Python](#Python)
* [C++](#C++)

"geometricConstraints\_var" is a variable referencing a [GeometricConstraints](GeometricConstraints.htm) object.```` ``` returnValue = geometricConstraints_var.addPerpendicularToSurface(curve, surface) ``` ```` |

"geometricConstraints\_var" is a variable referencing a [GeometricConstraints](GeometricConstraints.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [PerpendicularToSurfaceConstraint](PerpendicularToSurfaceConstraint.htm) | Returns the newly created PerpendicularToSurfaceConstraint object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| curve | [SketchCurve](SketchCurve.htm) | The SketchCurve to constrain to the surface. |
| surface | [Base](Base.htm) | The BRepFace or ConstructionPlane the line will be perpendicular to. |

## Version

Introduced in version September 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
# GeometricConstraints.addCoincidentToSurface Method

Parent Object: [GeometricConstraints](GeometricConstraints.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/GeometricConstraints.h>

## Description

Creates a new coincident constraint between the sketch point and surface. This forces the point to lie on the surface.

## Syntax

* [Python](#Python)
* [C++](#C++)

"geometricConstraints\_var" is a variable referencing a [GeometricConstraints](GeometricConstraints.htm) object.```` ``` returnValue = geometricConstraints_var.addCoincidentToSurface(point, surface) ``` ```` |

"geometricConstraints\_var" is a variable referencing a [GeometricConstraints](GeometricConstraints.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [CoincidentToSurfaceConstraint](CoincidentToSurfaceConstraint.htm) | Returns the newly created CoincidentToSurfaceConstraint object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| point | [SketchPoint](SketchPoint.htm) | The SketchPoint to constrain to the surface. |
| surface | [Base](Base.htm) | The BRepFace or ConstructionPlane the point will be coincident to. |

## Version

Introduced in version September 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
# GeometricConstraints.addConcentric Method

Parent Object: [GeometricConstraints](GeometricConstraints.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/GeometricConstraints.h>

## Description

Creates a new concentric constraint between two circles, arcs, ellipses, or elliptical arcs.

## Syntax

* [Python](#Python)
* [C++](#C++)

"geometricConstraints\_var" is a variable referencing a [GeometricConstraints](GeometricConstraints.htm) object.```` ``` returnValue = geometricConstraints_var.addConcentric(entityOne, entityTwo) ``` ```` |

"geometricConstraints\_var" is a variable referencing a [GeometricConstraints](GeometricConstraints.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ConcentricConstraint](ConcentricConstraint.htm) | Returns the newly created ConcentricConstraint object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| entityOne | [SketchCurve](SketchCurve.htm) | The first circle, arc, ellipse or elliptical arc. |
| entityTwo | [SketchCurve](SketchCurve.htm) | The second circle, arc, ellipse or elliptical arc. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [GeometricConstraints.addConcentric](GeometricConstraints_addConcentric_Sample.htm) | Demonstrates the GeometricConstraints.addConcentric method. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
# GeometricConstraints.addSmooth Method

Parent Object: [GeometricConstraints](GeometricConstraints.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/GeometricConstraints.h>

## Description

Creates a new smooth constraint between two curves. One of the curves must be a spline. The other curve can be a spline or any other type of curve.

## Syntax

* [Python](#Python)
* [C++](#C++)

"geometricConstraints\_var" is a variable referencing a [GeometricConstraints](GeometricConstraints.htm) object.```` ``` returnValue = geometricConstraints_var.addSmooth(curveOne, curveTwo) ``` ```` |

"geometricConstraints\_var" is a variable referencing a [GeometricConstraints](GeometricConstraints.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [SmoothConstraint](SmoothConstraint.htm) | Returns the newly created SmoothConstraint object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| curveOne | [SketchCurve](SketchCurve.htm) | The first curve to be constrained to be smooth to the second curve. |
| curveTwo | [SketchCurve](SketchCurve.htm) | The second curve to be constrained to be smooth to the first curve. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [GeometricConstraints.addSmooth](GeometricConstraints_addSmooth_Sample.htm) | Demonstrate the GeometricConstraints.addSmooth method. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
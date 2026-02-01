# GeometricConstraints.addTangent Method

Parent Object: [GeometricConstraints](GeometricConstraints.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/GeometricConstraints.h>

## Description

Creates a new tangent constraint between two curves.

## Syntax

* [Python](#Python)
* [C++](#C++)

"geometricConstraints\_var" is a variable referencing a [GeometricConstraints](GeometricConstraints.htm) object.```` ``` returnValue = geometricConstraints_var.addTangent(curveOne, curveTwo) ``` ```` |

"geometricConstraints\_var" is a variable referencing a [GeometricConstraints](GeometricConstraints.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [TangentConstraint](TangentConstraint.htm) | Returns the newly created TangentConstraint object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| curveOne | [SketchCurve](SketchCurve.htm) | The first curve to be tangent. |
| curveTwo | [SketchCurve](SketchCurve.htm) | The second curve to be tangent. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create Circle By 3 Tangents API Sample](CreateCcircleBy3Tangents_Sample.htm) | Creates three lines and then draws a circle that is tangent to the lines. It then creates tangent constraints to maintain that relationship. |
| [GeometricConstraints.addTangent](GeometricConstraints_addTangent_Sample.htm) | Demonstrates the GeometricConstraints.addTangent method. |
| [SketchCircles.addByTwoTangents](SketchCircles_addByTwoTangents_Sample.htm) | Demonstrates the SketchCircles.addByTwoTangets method. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
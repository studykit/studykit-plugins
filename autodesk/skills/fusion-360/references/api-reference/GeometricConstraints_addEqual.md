# GeometricConstraints.addEqual Method

Parent Object: [GeometricConstraints](GeometricConstraints.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/GeometricConstraints.h>

## Description

Creates a new equal constraint between two lines, or between arcs and circles.

## Syntax

* [Python](#Python)
* [C++](#C++)

"geometricConstraints\_var" is a variable referencing a [GeometricConstraints](GeometricConstraints.htm) object.```` ``` returnValue = geometricConstraints_var.addEqual(curveOne, curveTwo) ``` ```` |

"geometricConstraints\_var" is a variable referencing a [GeometricConstraints](GeometricConstraints.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [EqualConstraint](EqualConstraint.htm) | Returns the newly created EqualConstraint object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| curveOne | [SketchCurve](SketchCurve.htm) | The first line, arc, or circle. |
| curveTwo | [SketchCurve](SketchCurve.htm) | The second line, arc, or circle. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [GeometricConstraints.addEqual](GeometricConstraints_addEqual_Sample.htm) | Demonstrates the GeometricConstraints.addEqual method. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
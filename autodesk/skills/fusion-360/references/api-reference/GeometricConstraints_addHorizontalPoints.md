# GeometricConstraints.addHorizontalPoints Method

Parent Object: [GeometricConstraints](GeometricConstraints.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/GeometricConstraints.h>

## Description

Creates a new horizontal constraint between two points.

## Syntax

* [Python](#Python)
* [C++](#C++)

"geometricConstraints\_var" is a variable referencing a [GeometricConstraints](GeometricConstraints.htm) object.```` ``` returnValue = geometricConstraints_var.addHorizontalPoints(pointOne, pointTwo) ``` ```` |

"geometricConstraints\_var" is a variable referencing a [GeometricConstraints](GeometricConstraints.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [HorizontalPointsConstraint](HorizontalPointsConstraint.htm) | Returns the newly created HorizontalPointsConstraint object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| pointOne | [SketchPoint](SketchPoint.htm) | The first SketchPoint to constrain horizontally. |
| pointTwo | [SketchPoint](SketchPoint.htm) | The second SketchPoint to constrain horizontally. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [GeometricConstraint.addHorizontalPoints](GeometricConstraint_addHorizontalPoints_Sample.htm) | Demonstrates the GeometricConstraint.addHorizontalPoints method. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
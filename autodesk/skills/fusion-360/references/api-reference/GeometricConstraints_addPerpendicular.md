# GeometricConstraints.addPerpendicular Method

Parent Object: [GeometricConstraints](GeometricConstraints.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/GeometricConstraints.h>

## Description

Creates a new perpendicular constraint between two lines.

## Syntax

* [Python](#Python)
* [C++](#C++)

"geometricConstraints\_var" is a variable referencing a [GeometricConstraints](GeometricConstraints.htm) object.```` ``` returnValue = geometricConstraints_var.addPerpendicular(lineOne, lineTwo) ``` ```` |

"geometricConstraints\_var" is a variable referencing a [GeometricConstraints](GeometricConstraints.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [PerpendicularConstraint](PerpendicularConstraint.htm) | Returns the newly created PerpendicularConstraint object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| lineOne | [SketchLine](SketchLine.htm) | The first SketchLine. |
| lineTwo | [SketchLine](SketchLine.htm) | The second SketchLine. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [GeometricConstraints.addPerpendicular](GeometricConstraints_addPerpendicular_Sample.htm) | Demonstrates the GeometricConstraints.addPerpendicular method. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
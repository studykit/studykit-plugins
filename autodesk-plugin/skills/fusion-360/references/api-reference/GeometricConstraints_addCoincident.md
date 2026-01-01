# GeometricConstraints.addCoincident Method

Parent Object: [GeometricConstraints](GeometricConstraints.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/GeometricConstraints.h>

## Description

Creates a new coincident constraint between two entities. The first argument is a sketch point. The second argument is a sketch curve or point.

## Syntax

* [Python](#Python)
* [C++](#C++)

"geometricConstraints\_var" is a variable referencing a [GeometricConstraints](GeometricConstraints.htm) object.```` ``` returnValue = geometricConstraints_var.addCoincident(point, entity) ``` ```` |

"geometricConstraints\_var" is a variable referencing a [GeometricConstraints](GeometricConstraints.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [CoincidentConstraint](CoincidentConstraint.htm) | Returns the newly created CoincidentConstraint object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| point | [SketchPoint](SketchPoint.htm) | The SketchPoint that will be made coincident. |
| entity | [SketchEntity](SketchEntity.htm) | The SketchPoint or sketch curve that the point will be made coincident to. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [GeometricConstraints.addCoincident](GeometricConstraints_addCoincident_Sample.htm) | Demonstrates the GeometricConstraints.addCoincident method. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
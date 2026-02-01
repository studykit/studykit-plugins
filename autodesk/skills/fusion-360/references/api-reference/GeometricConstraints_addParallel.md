# GeometricConstraints.addParallel Method

Parent Object: [GeometricConstraints](GeometricConstraints.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/GeometricConstraints.h>

## Description

Creates a new parallel constraint between two lines.

## Syntax

* [Python](#Python)
* [C++](#C++)

"geometricConstraints\_var" is a variable referencing a [GeometricConstraints](GeometricConstraints.htm) object.```` ``` returnValue = geometricConstraints_var.addParallel(lineOne, lineTwo) ``` ```` |

"geometricConstraints\_var" is a variable referencing a [GeometricConstraints](GeometricConstraints.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ParallelConstraint](ParallelConstraint.htm) | Returns the newly created ParallelConstraint object or null if the creation failed. |

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
| [GeometricConstraints.addParallel](GeometricConstraints_addParallel_Sample.htm) | Demonstrate the GeometricConstraints.addParallel method. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
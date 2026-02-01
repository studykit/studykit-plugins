# GeometricConstraints.addSymmetry Method

Parent Object: [GeometricConstraints](GeometricConstraints.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/GeometricConstraints.h>

## Description

Creates a new symmetry constraint.

## Syntax

* [Python](#Python)
* [C++](#C++)

"geometricConstraints\_var" is a variable referencing a [GeometricConstraints](GeometricConstraints.htm) object.```` ``` returnValue = geometricConstraints_var.addSymmetry(entityOne, entityTwo, symmetryLine) ``` ```` |

"geometricConstraints\_var" is a variable referencing a [GeometricConstraints](GeometricConstraints.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [SymmetryConstraint](SymmetryConstraint.htm) | Returns the newly created SymmetryConstraint object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| entityOne | [SketchEntity](SketchEntity.htm) | The first sketch entity to be symmetric. |
| entityTwo | [SketchEntity](SketchEntity.htm) | The second sketch entity to be symmetric. It must be the same type as the first entity. |
| symmetryLine | [SketchLine](SketchLine.htm) | The SketchLine that defines the axis of symmetry. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [GeometricConstraints.addSymmetry](GeometricConstraints_addSymmetry_Sample.htm) | Demonstrates the GeometricConstraints.addSymmetry method. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
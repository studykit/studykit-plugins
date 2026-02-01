# GeometricConstraints.addCollinear Method

Parent Object: [GeometricConstraints](GeometricConstraints.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/GeometricConstraints.h>

## Description

Creates a new collinear constraint between two lines.

## Syntax

* [Python](#Python)
* [C++](#C++)

"geometricConstraints\_var" is a variable referencing a [GeometricConstraints](GeometricConstraints.htm) object.```` ``` returnValue = geometricConstraints_var.addCollinear(lineOne, lineTwo) ``` ```` |

"geometricConstraints\_var" is a variable referencing a [GeometricConstraints](GeometricConstraints.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [CollinearConstraint](CollinearConstraint.htm) | Returns the newly created CollinearConstraint object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| lineOne | [SketchLine](SketchLine.htm) | The first line to create the constraint on. |
| lineTwo | [SketchLine](SketchLine.htm) | The second line to create the constraint on. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [GeometricConstraints.addCollinear](GeometricConstraints_addCollinear_Sample.htm) | Demonstrates the GeometricConstraints.addCollinear method. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
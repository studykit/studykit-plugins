# GeometricConstraints.addHorizontal Method

Parent Object: [GeometricConstraints](GeometricConstraints.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/GeometricConstraints.h>

## Description

Creates a new horizontal constraint on a line.

## Syntax

* [Python](#Python)
* [C++](#C++)

"geometricConstraints\_var" is a variable referencing a [GeometricConstraints](GeometricConstraints.htm) object.```` ``` returnValue = geometricConstraints_var.addHorizontal(line) ``` ```` |

"geometricConstraints\_var" is a variable referencing a [GeometricConstraints](GeometricConstraints.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [HorizontalConstraint](HorizontalConstraint.htm) | Returns the newly created HorizontalConstraint object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| line | [SketchLine](SketchLine.htm) | The line to constrain horizontally. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [API Sample that demonstrates creating sketch lines in various ways.](CreateSketchLines_Sample.htm) | Demonstrates several ways to create sketch lines, including as the result of creating a rectangle. |
| [GeometricConstraint.addHorizontal](GeometricConstraint_addHorizontal_Sample.htm) | Demonstrates the GeometricConstraint.addHorizontal method. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
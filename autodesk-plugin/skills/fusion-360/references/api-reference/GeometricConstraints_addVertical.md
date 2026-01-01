# GeometricConstraints.addVertical Method

Parent Object: [GeometricConstraints](GeometricConstraints.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/GeometricConstraints.h>

## Description

Creates a new vertical constraint on a line.

## Syntax

* [Python](#Python)
* [C++](#C++)

"geometricConstraints\_var" is a variable referencing a [GeometricConstraints](GeometricConstraints.htm) object.```` ``` returnValue = geometricConstraints_var.addVertical(line) ``` ```` |

"geometricConstraints\_var" is a variable referencing a [GeometricConstraints](GeometricConstraints.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [VerticalConstraint](VerticalConstraint.htm) | Returns the newly created VerticalConstraint object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| line | [SketchLine](SketchLine.htm) | The line to constrain vertically. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [API Sample that demonstrates creating sketch lines in various ways.](CreateSketchLines_Sample.htm) | Demonstrates several ways to create sketch lines, including as the result of creating a rectangle. |
| [GeometricConstraints.addVertical](GeometricConstraints_addVertical_Sample.htm) | Demonstrates the GeometricConstraints.addVertical method. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
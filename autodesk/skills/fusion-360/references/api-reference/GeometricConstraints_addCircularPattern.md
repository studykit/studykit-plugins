# GeometricConstraints.addCircularPattern Method

Parent Object: [GeometricConstraints](GeometricConstraints.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/GeometricConstraints.h>

## Description

Creates a new circular pattern in the sketch.

## Syntax

* [Python](#Python)
* [C++](#C++)

"geometricConstraints\_var" is a variable referencing a [GeometricConstraints](GeometricConstraints.htm) object.```` ``` returnValue = geometricConstraints_var.addCircularPattern(input) ``` ```` |

"geometricConstraints\_var" is a variable referencing a [GeometricConstraints](GeometricConstraints.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [CircularPatternConstraint](CircularPatternConstraint.htm) | Returns the newly created CircularPatternConstraint object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| input | [CircularPatternConstraintInput](CircularPatternConstraintInput.htm) | A CircularPatternConstraintInput object that defines the desired circular pattern. Use the createCircularPatternInput method to create a new CircularPatternConstraintInput object and then use methods on it to define the circular pattern. |

## Version

Introduced in version September 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
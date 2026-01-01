# GeometricConstraints.createCircularPatternInput Method

Parent Object: [GeometricConstraints](GeometricConstraints.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/GeometricConstraints.h>

## Description

Creates a CircularPatternConstraintInput object. Use properties and methods on this object to define the circular pattern you want to create and then use the Add method, passing in the CircularPatternConstraintInput object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"geometricConstraints\_var" is a variable referencing a [GeometricConstraints](GeometricConstraints.htm) object.```` ``` returnValue = geometricConstraints_var.createCircularPatternInput(inputEntities, centerPoint) ``` ```` |

"geometricConstraints\_var" is a variable referencing a [GeometricConstraints](GeometricConstraints.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [CircularPatternConstraintInput](CircularPatternConstraintInput.htm) | Returns the newly created CircularPatternConstraintInput object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| inputEntities | SketchEntity[] | An array of sketch entities to be patterned. All of the entities must be from the current sketch. |
| centerPoint | [SketchPoint](SketchPoint.htm) | A SketchPoint from the same sketch that defines the center of the pattern. |

## Version

Introduced in version September 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
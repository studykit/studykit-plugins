# RectangularPatternConstraintInput.setDirectionOne Method

Parent Object: [RectangularPatternConstraintInput](RectangularPatternConstraintInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/RectangularPatternConstraintInput.h>

## Description

Sets all of the input required to define the pattern in the first direction.

## Syntax

* [Python](#Python)
* [C++](#C++)

"rectangularPatternConstraintInput\_var" is a variable referencing a [RectangularPatternConstraintInput](RectangularPatternConstraintInput.htm) object.```` ``` returnValue = rectangularPatternConstraintInput_var.setDirectionOne(directionOneEntity, quantityOne, distanceOne) ``` ```` |

"rectangularPatternConstraintInput\_var" is a variable referencing a [RectangularPatternConstraintInput](RectangularPatternConstraintInput.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if it was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| directionOneEntity | [SketchLine](SketchLine.htm) | Specifies the SketchLine object used to define the first direction entity.   This argument can be null to indicate that the default first direction is to be used, which is along the X axis of the sketch. |
| quantityOne | [ValueInput](ValueInput.htm) | Specifies the number of instances in the first direction. |
| distanceOne | [ValueInput](ValueInput.htm) | Specifies the distance in the first direction. How this value is used depends on the value of the PatternDistanceType property. If the value is ExtentPatternDistanceType then it defines the total distance of the pattern. If the value is SpacingPatternDistanceType then it defines the distance between each element. |

## Version

Introduced in version September 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
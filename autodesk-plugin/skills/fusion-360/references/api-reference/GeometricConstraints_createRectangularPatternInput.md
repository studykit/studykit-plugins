# GeometricConstraints.createRectangularPatternInput Method

Parent Object: [GeometricConstraints](GeometricConstraints.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/GeometricConstraints.h>

## Description

Creates a new RectangularPatternConstraintInput object. Use this object to define the various settings associated with a rectangular pattern in a sketch. Once the pattern is defined you can call the addRectangularPattern method and pass in the input object to create the sketch rectangular pattern.

## Syntax

* [Python](#Python)
* [C++](#C++)

"geometricConstraints\_var" is a variable referencing a [GeometricConstraints](GeometricConstraints.htm) object.```` ``` returnValue = geometricConstraints_var.createRectangularPatternInput(entities, distanceType) ``` ```` |

"geometricConstraints\_var" is a variable referencing a [GeometricConstraints](GeometricConstraints.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [RectangularPatternConstraintInput](RectangularPatternConstraintInput.htm) | Returns the created RectangularPatternsConstraintInput object or null in the case of failure. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| entities | SketchEntity[] | An array of sketch entities to pattern. These can be sketch points and curves. |
| distanceType | [PatternDistanceType](PatternDistanceType.htm) | Specifies if the distances defined for the pattern define the overall size of the pattern or the distance between the rows and columns. |

## Version

Introduced in version September 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
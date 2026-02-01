# RectangularPatternConstraintInput.distanceType Property

Parent Object: [RectangularPatternConstraintInput](RectangularPatternConstraintInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/RectangularPatternConstraintInput.h>

## Description

Gets and sets how the distance between elements is computed.

## Syntax

* [Python](#Python)
* [C++](#C++)

"rectangularPatternConstraintInput\_var" is a variable referencing a RectangularPatternConstraintInput object. |

"rectangularPatternConstraintInput\_var" is a variable referencing a RectangularPatternConstraintInput object. ```` ``` #include <Fusion/Sketch/RectangularPatternConstraintInput.h>  // Get the value of the property. PatternDistanceType propertyValue = rectangularPatternConstraintInput_var->distanceType();  // Set the value of the property, where value_var is a PatternDistanceType. bool returnValue = rectangularPatternConstraintInput_var->distanceType(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [PatternDistanceType](PatternDistanceType.htm).

## Version

Introduced in version September 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
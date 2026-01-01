# RectangularPatternConstraintInput.distanceTwo Property

Parent Object: [RectangularPatternConstraintInput](RectangularPatternConstraintInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/RectangularPatternConstraintInput.h>

## Description

Gets and sets the distance in the second direction.

## Syntax

* [Python](#Python)
* [C++](#C++)

"rectangularPatternConstraintInput\_var" is a variable referencing a RectangularPatternConstraintInput object. |

"rectangularPatternConstraintInput\_var" is a variable referencing a RectangularPatternConstraintInput object. ```` ``` #include <Fusion/Sketch/RectangularPatternConstraintInput.h>  // Get the value of the property. Ptr<ValueInput> propertyValue = rectangularPatternConstraintInput_var->distanceTwo();  // Set the value of the property, where value_var is a ValueInput. bool returnValue = rectangularPatternConstraintInput_var->distanceTwo(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [ValueInput](ValueInput.htm).

## Version

Introduced in version September 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
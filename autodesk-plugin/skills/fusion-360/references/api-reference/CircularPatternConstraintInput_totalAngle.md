# CircularPatternConstraintInput.totalAngle Property

Parent Object: [CircularPatternConstraintInput](CircularPatternConstraintInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/CircularPatternConstraintInput.h>

## Description

Gets and sets total angle. A positive angle is a counter-clockwise direction and a negative angle can be used to reverse the direction. An angle of 360 degrees or 2 pi radians will create a full circular pattern.

## Syntax

* [Python](#Python)
* [C++](#C++)

"circularPatternConstraintInput\_var" is a variable referencing a CircularPatternConstraintInput object. |

"circularPatternConstraintInput\_var" is a variable referencing a CircularPatternConstraintInput object. ```` ``` #include <Fusion/Sketch/CircularPatternConstraintInput.h>  // Get the value of the property. Ptr<ValueInput> propertyValue = circularPatternConstraintInput_var->totalAngle();  // Set the value of the property, where value_var is a ValueInput. bool returnValue = circularPatternConstraintInput_var->totalAngle(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [ValueInput](ValueInput.htm).

## Version

Introduced in version September 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
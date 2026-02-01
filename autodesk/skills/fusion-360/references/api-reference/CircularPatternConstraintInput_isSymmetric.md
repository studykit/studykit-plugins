# CircularPatternConstraintInput.isSymmetric Property

Parent Object: [CircularPatternConstraintInput](CircularPatternConstraintInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/CircularPatternConstraintInput.h>

## Description

Gets and sets if the angle extent is in one direction or is symmetric.

## Syntax

* [Python](#Python)
* [C++](#C++)

"circularPatternConstraintInput\_var" is a variable referencing a CircularPatternConstraintInput object. |

"circularPatternConstraintInput\_var" is a variable referencing a CircularPatternConstraintInput object. ```` ``` #include <Fusion/Sketch/CircularPatternConstraintInput.h>  // Get the value of the property. boolean propertyValue = circularPatternConstraintInput_var->isSymmetric();  // Set the value of the property, where value_var is a boolean. bool returnValue = circularPatternConstraintInput_var->isSymmetric(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version September 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
# CircularPatternConstraintInput.isSuppressed Property

Parent Object: [CircularPatternConstraintInput](CircularPatternConstraintInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/CircularPatternConstraintInput.h>

## Description

Specifies which, if any, instances of the pattern are suppressed. This defaults to all instances being visible. This returns an array of Booleans that indicates if a particular instance in the pattern is suppressed or not. A value of true will result in the associated instance being suppressed.

## Syntax

* [Python](#Python)
* [C++](#C++)

"circularPatternConstraintInput\_var" is a variable referencing a CircularPatternConstraintInput object. |

"circularPatternConstraintInput\_var" is a variable referencing a CircularPatternConstraintInput object. ```` ``` #include <Fusion/Sketch/CircularPatternConstraintInput.h>  // Get the value of the property. std::vector<boolean> propertyValue = circularPatternConstraintInput_var->isSuppressed();  // Set the value of the property, where value_var is a boolean. bool returnValue = circularPatternConstraintInput_var->isSuppressed(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an array of type boolean.

## Version

Introduced in version September 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
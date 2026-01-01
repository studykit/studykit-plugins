# RectangularPatternConstraintInput.isSuppressed Property

Parent Object: [RectangularPatternConstraintInput](RectangularPatternConstraintInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/RectangularPatternConstraintInput.h>

## Description

Specifies which, if any, instances of the pattern are suppressed. This defaults to all instances being visible. This returns an array of Booleans that indicates if a particular instance in the pattern is suppressed or not. A value of true will result in the associated instance being suppressed.

## Syntax

* [Python](#Python)
* [C++](#C++)

"rectangularPatternConstraintInput\_var" is a variable referencing a RectangularPatternConstraintInput object.  ```` ``` # Get the value of the property. propertyValue = rectangularPatternConstraintInput_var.isSuppressed  # Set the value of the property. rectangularPatternConstraintInput_var.isSuppressed = propertyValue ``` ```` |

"rectangularPatternConstraintInput\_var" is a variable referencing a RectangularPatternConstraintInput object. ```` ``` #include <Fusion/Sketch/RectangularPatternConstraintInput.h>  // Get the value of the property. std::vector<boolean> propertyValue = rectangularPatternConstraintInput_var->isSuppressed();  // Set the value of the property, where value_var is a boolean. bool returnValue = rectangularPatternConstraintInput_var->isSuppressed(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an array of type boolean.

## Version

Introduced in version September 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
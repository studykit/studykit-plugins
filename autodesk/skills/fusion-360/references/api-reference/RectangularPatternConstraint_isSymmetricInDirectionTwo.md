# RectangularPatternConstraint.isSymmetricInDirectionTwo Property

Parent Object: [RectangularPatternConstraint](RectangularPatternConstraint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/RectangularPatternConstraint.h>

## Description

Gets and sets if the pattern in direction two is in one direction or is symmetric.

## Syntax

* [Python](#Python)
* [C++](#C++)

"rectangularPatternConstraint\_var" is a variable referencing a RectangularPatternConstraint object. |

"rectangularPatternConstraint\_var" is a variable referencing a RectangularPatternConstraint object. ```` ``` #include <Fusion/Sketch/RectangularPatternConstraint.h>  // Get the value of the property. boolean propertyValue = rectangularPatternConstraint_var->isSymmetricInDirectionTwo();  // Set the value of the property, where value_var is a boolean. bool returnValue = rectangularPatternConstraint_var->isSymmetricInDirectionTwo(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version September 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
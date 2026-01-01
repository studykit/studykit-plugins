# CircularPatternConstraint.isSuppressed Property

Parent Object: [CircularPatternConstraint](CircularPatternConstraint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/CircularPatternConstraint.h>

## Description

Specifies which, if any, instances of the pattern are suppressed. This returns an array of Boolean values that indicates if a particular instance in the pattern is suppressed or not. A value of true will result in the associated instance being suppressed.

## Syntax

* [Python](#Python)
* [C++](#C++)

"circularPatternConstraint\_var" is a variable referencing a CircularPatternConstraint object. |

"circularPatternConstraint\_var" is a variable referencing a CircularPatternConstraint object. ```` ``` #include <Fusion/Sketch/CircularPatternConstraint.h>  // Get the value of the property. std::vector<boolean> propertyValue = circularPatternConstraint_var->isSuppressed();  // Set the value of the property, where value_var is a boolean. bool returnValue = circularPatternConstraint_var->isSuppressed(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an array of type boolean.

## Version

Introduced in version September 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
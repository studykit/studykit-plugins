# CircularPatternConstraint.attributes Property

Parent Object: [CircularPatternConstraint](CircularPatternConstraint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/CircularPatternConstraint.h>

## Description

Returns the collection of attributes associated with this geometric constraint.

## Syntax

* [Python](#Python)
* [C++](#C++)

"circularPatternConstraint\_var" is a variable referencing a CircularPatternConstraint object. |

"circularPatternConstraint\_var" is a variable referencing a CircularPatternConstraint object. ```` ``` #include <Fusion/Sketch/CircularPatternConstraint.h>  // Get the value of the property. Ptr<Attributes> propertyValue = circularPatternConstraint_var->attributes(); ``` ```` |

## Property Value

This is a read only property whose value is an [Attributes](Attributes.htm).

## Version

Introduced in version May 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
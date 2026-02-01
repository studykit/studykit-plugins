# EqualConstraint.parentSketch Property

Parent Object: [EqualConstraint](EqualConstraint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/EqualConstraint.h>

## Description

Returns the parent sketch object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"equalConstraint\_var" is a variable referencing an EqualConstraint object. |

"equalConstraint\_var" is a variable referencing an EqualConstraint object. ```` ``` #include <Fusion/Sketch/EqualConstraint.h>  // Get the value of the property. Ptr<Sketch> propertyValue = equalConstraint_var->parentSketch(); ``` ```` |

## Property Value

This is a read only property whose value is a [Sketch](Sketch.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
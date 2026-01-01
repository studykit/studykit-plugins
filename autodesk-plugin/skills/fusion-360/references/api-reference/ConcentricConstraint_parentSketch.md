# ConcentricConstraint.parentSketch Property

Parent Object: [ConcentricConstraint](ConcentricConstraint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/ConcentricConstraint.h>

## Description

Returns the parent sketch object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"concentricConstraint\_var" is a variable referencing a ConcentricConstraint object. |

"concentricConstraint\_var" is a variable referencing a ConcentricConstraint object. ```` ``` #include <Fusion/Sketch/ConcentricConstraint.h>  // Get the value of the property. Ptr<Sketch> propertyValue = concentricConstraint_var->parentSketch(); ``` ```` |

## Property Value

This is a read only property whose value is a [Sketch](Sketch.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
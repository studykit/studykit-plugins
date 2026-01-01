# CollinearConstraint.parentSketch Property

Parent Object: [CollinearConstraint](CollinearConstraint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/CollinearConstraint.h>

## Description

Returns the parent sketch object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"collinearConstraint\_var" is a variable referencing a CollinearConstraint object. |

"collinearConstraint\_var" is a variable referencing a CollinearConstraint object. ```` ``` #include <Fusion/Sketch/CollinearConstraint.h>  // Get the value of the property. Ptr<Sketch> propertyValue = collinearConstraint_var->parentSketch(); ``` ```` |

## Property Value

This is a read only property whose value is a [Sketch](Sketch.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
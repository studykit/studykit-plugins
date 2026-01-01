# SymmetryConstraint.symmetryLine Property

Parent Object: [SymmetryConstraint](SymmetryConstraint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SymmetryConstraint.h>

## Description

Returns the axis (SketchLine) that defines the symmetry.

## Syntax

* [Python](#Python)
* [C++](#C++)

"symmetryConstraint\_var" is a variable referencing a SymmetryConstraint object. |

"symmetryConstraint\_var" is a variable referencing a SymmetryConstraint object. ```` ``` #include <Fusion/Sketch/SymmetryConstraint.h>  // Get the value of the property. Ptr<SketchLine> propertyValue = symmetryConstraint_var->symmetryLine(); ``` ```` |

## Property Value

This is a read only property whose value is a [SketchLine](SketchLine.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
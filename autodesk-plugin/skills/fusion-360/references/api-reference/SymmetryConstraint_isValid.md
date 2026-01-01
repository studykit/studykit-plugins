# SymmetryConstraint.isValid Property

Parent Object: [SymmetryConstraint](SymmetryConstraint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SymmetryConstraint.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"symmetryConstraint\_var" is a variable referencing a SymmetryConstraint object. |

"symmetryConstraint\_var" is a variable referencing a SymmetryConstraint object. ```` ``` #include <Fusion/Sketch/SymmetryConstraint.h>  // Get the value of the property. boolean propertyValue = symmetryConstraint_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
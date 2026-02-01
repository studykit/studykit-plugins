# SymmetryConstraint.nativeObject Property

Parent Object: [SymmetryConstraint](SymmetryConstraint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SymmetryConstraint.h>

## Description

The NativeObject is the object outside the context of an assembly and in the context of it's parent component. Returns null in the case where this object is not in the context of an assembly but is already the native object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"symmetryConstraint\_var" is a variable referencing a SymmetryConstraint object. |

"symmetryConstraint\_var" is a variable referencing a SymmetryConstraint object. ```` ``` #include <Fusion/Sketch/SymmetryConstraint.h>  // Get the value of the property. Ptr<SymmetryConstraint> propertyValue = symmetryConstraint_var->nativeObject(); ``` ```` |

## Property Value

This is a read only property whose value is a [SymmetryConstraint](SymmetryConstraint.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
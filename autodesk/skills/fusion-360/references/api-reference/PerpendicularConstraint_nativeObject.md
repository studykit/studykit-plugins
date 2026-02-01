# PerpendicularConstraint.nativeObject Property

Parent Object: [PerpendicularConstraint](PerpendicularConstraint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/PerpendicularConstraint.h>

## Description

The NativeObject is the object outside the context of an assembly and in the context of it's parent component. Returns null in the case where this object is not in the context of an assembly but is already the native object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"perpendicularConstraint\_var" is a variable referencing a PerpendicularConstraint object. |

"perpendicularConstraint\_var" is a variable referencing a PerpendicularConstraint object. ```` ``` #include <Fusion/Sketch/PerpendicularConstraint.h>  // Get the value of the property. Ptr<PerpendicularConstraint> propertyValue = perpendicularConstraint_var->nativeObject(); ``` ```` |

## Property Value

This is a read only property whose value is a [PerpendicularConstraint](PerpendicularConstraint.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
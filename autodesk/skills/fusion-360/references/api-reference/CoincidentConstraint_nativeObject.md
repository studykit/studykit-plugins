# CoincidentConstraint.nativeObject Property

Parent Object: [CoincidentConstraint](CoincidentConstraint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/CoincidentConstraint.h>

## Description

The NativeObject is the object outside the context of an assembly and in the context of it's parent component. Returns null in the case where this object is not in the context of an assembly but is already the native object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"coincidentConstraint\_var" is a variable referencing a CoincidentConstraint object. |

"coincidentConstraint\_var" is a variable referencing a CoincidentConstraint object. ```` ``` #include <Fusion/Sketch/CoincidentConstraint.h>  // Get the value of the property. Ptr<CoincidentConstraint> propertyValue = coincidentConstraint_var->nativeObject(); ``` ```` |

## Property Value

This is a read only property whose value is a [CoincidentConstraint](CoincidentConstraint.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
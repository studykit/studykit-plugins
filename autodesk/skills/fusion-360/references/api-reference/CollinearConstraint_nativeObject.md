# CollinearConstraint.nativeObject Property

Parent Object: [CollinearConstraint](CollinearConstraint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/CollinearConstraint.h>

## Description

The NativeObject is the object outside the context of an assembly and in the context of it's parent component. Returns null in the case where this object is not in the context of an assembly but is already the native object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"collinearConstraint\_var" is a variable referencing a CollinearConstraint object. |

"collinearConstraint\_var" is a variable referencing a CollinearConstraint object. ```` ``` #include <Fusion/Sketch/CollinearConstraint.h>  // Get the value of the property. Ptr<CollinearConstraint> propertyValue = collinearConstraint_var->nativeObject(); ``` ```` |

## Property Value

This is a read only property whose value is a [CollinearConstraint](CollinearConstraint.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
# TangentConstraint.nativeObject Property

Parent Object: [TangentConstraint](TangentConstraint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/TangentConstraint.h>

## Description

The NativeObject is the object outside the context of an assembly and in the context of it's parent component. Returns null in the case where this object is not in the context of an assembly but is already the native object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"tangentConstraint\_var" is a variable referencing a TangentConstraint object. |

"tangentConstraint\_var" is a variable referencing a TangentConstraint object. ```` ``` #include <Fusion/Sketch/TangentConstraint.h>  // Get the value of the property. Ptr<TangentConstraint> propertyValue = tangentConstraint_var->nativeObject(); ``` ```` |

## Property Value

This is a read only property whose value is a [TangentConstraint](TangentConstraint.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
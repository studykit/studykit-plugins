# VerticalConstraint.nativeObject Property

Parent Object: [VerticalConstraint](VerticalConstraint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/VerticalConstraint.h>

## Description

The NativeObject is the object outside the context of an assembly and in the context of it's parent component. Returns null in the case where this object is not in the context of an assembly but is already the native object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"verticalConstraint\_var" is a variable referencing a VerticalConstraint object. |

"verticalConstraint\_var" is a variable referencing a VerticalConstraint object. ```` ``` #include <Fusion/Sketch/VerticalConstraint.h>  // Get the value of the property. Ptr<VerticalConstraint> propertyValue = verticalConstraint_var->nativeObject(); ``` ```` |

## Property Value

This is a read only property whose value is a [VerticalConstraint](VerticalConstraint.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
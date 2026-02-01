# OffsetConstraint.nativeObject Property

Parent Object: [OffsetConstraint](OffsetConstraint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/OffsetConstraint.h>

## Description

The NativeObject is the object outside the context of an assembly and in the context of it's parent component. Returns null in the case where this object is not in the context of an assembly but is already the native object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"offsetConstraint\_var" is a variable referencing an OffsetConstraint object. |

"offsetConstraint\_var" is a variable referencing an OffsetConstraint object. ```` ``` #include <Fusion/Sketch/OffsetConstraint.h>  // Get the value of the property. Ptr<OffsetConstraint> propertyValue = offsetConstraint_var->nativeObject(); ``` ```` |

## Property Value

This is a read only property whose value is an [OffsetConstraint](OffsetConstraint.htm).

## Version

Introduced in version May 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
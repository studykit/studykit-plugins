# MidPointConstraint.nativeObject Property

Parent Object: [MidPointConstraint](MidPointConstraint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/MidPointConstraint.h>

## Description

The NativeObject is the object outside the context of an assembly and in the context of it's parent component. Returns null in the case where this object is not in the context of an assembly but is already the native object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"midPointConstraint\_var" is a variable referencing a MidPointConstraint object. |

"midPointConstraint\_var" is a variable referencing a MidPointConstraint object. ```` ``` #include <Fusion/Sketch/MidPointConstraint.h>  // Get the value of the property. Ptr<MidPointConstraint> propertyValue = midPointConstraint_var->nativeObject(); ``` ```` |

## Property Value

This is a read only property whose value is a [MidPointConstraint](MidPointConstraint.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
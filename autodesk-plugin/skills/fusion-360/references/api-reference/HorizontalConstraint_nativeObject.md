# HorizontalConstraint.nativeObject Property

Parent Object: [HorizontalConstraint](HorizontalConstraint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/HorizontalConstraint.h>

## Description

The NativeObject is the object outside the context of an assembly and in the context of it's parent component. Returns null in the case where this object is not in the context of an assembly but is already the native object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"horizontalConstraint\_var" is a variable referencing a HorizontalConstraint object. |

"horizontalConstraint\_var" is a variable referencing a HorizontalConstraint object. ```` ``` #include <Fusion/Sketch/HorizontalConstraint.h>  // Get the value of the property. Ptr<HorizontalConstraint> propertyValue = horizontalConstraint_var->nativeObject(); ``` ```` |

## Property Value

This is a read only property whose value is a [HorizontalConstraint](HorizontalConstraint.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
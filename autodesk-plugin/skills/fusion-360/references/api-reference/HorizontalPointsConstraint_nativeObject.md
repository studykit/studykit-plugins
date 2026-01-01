# HorizontalPointsConstraint.nativeObject Property

Parent Object: [HorizontalPointsConstraint](HorizontalPointsConstraint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/HorizontalPointsConstraint.h>

## Description

The NativeObject is the object outside the context of an assembly and in the context of it's parent component. Returns null in the case where this object is not in the context of an assembly but is already the native object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"horizontalPointsConstraint\_var" is a variable referencing a HorizontalPointsConstraint object. |

"horizontalPointsConstraint\_var" is a variable referencing a HorizontalPointsConstraint object. ```` ``` #include <Fusion/Sketch/HorizontalPointsConstraint.h>  // Get the value of the property. Ptr<HorizontalPointsConstraint> propertyValue = horizontalPointsConstraint_var->nativeObject(); ``` ```` |

## Property Value

This is a read only property whose value is a [HorizontalPointsConstraint](HorizontalPointsConstraint.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
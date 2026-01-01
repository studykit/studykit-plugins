# VerticalPointsConstraint.nativeObject Property

Parent Object: [VerticalPointsConstraint](VerticalPointsConstraint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/VerticalPointsConstraint.h>

## Description

The NativeObject is the object outside the context of an assembly and in the context of it's parent component. Returns null in the case where this object is not in the context of an assembly but is already the native object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"verticalPointsConstraint\_var" is a variable referencing a VerticalPointsConstraint object. |

"verticalPointsConstraint\_var" is a variable referencing a VerticalPointsConstraint object. ```` ``` #include <Fusion/Sketch/VerticalPointsConstraint.h>  // Get the value of the property. Ptr<VerticalPointsConstraint> propertyValue = verticalPointsConstraint_var->nativeObject(); ``` ```` |

## Property Value

This is a read only property whose value is a [VerticalPointsConstraint](VerticalPointsConstraint.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
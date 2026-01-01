# RectangularPatternConstraint.nativeObject Property

Parent Object: [RectangularPatternConstraint](RectangularPatternConstraint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/RectangularPatternConstraint.h>

## Description

The NativeObject is the object outside the context of an assembly and in the context of it's parent component. Returns null in the case where this object is not in the context of an assembly but is already the native object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"rectangularPatternConstraint\_var" is a variable referencing a RectangularPatternConstraint object. |

"rectangularPatternConstraint\_var" is a variable referencing a RectangularPatternConstraint object. ```` ``` #include <Fusion/Sketch/RectangularPatternConstraint.h>  // Get the value of the property. Ptr<RectangularPatternConstraint> propertyValue = rectangularPatternConstraint_var->nativeObject(); ``` ```` |

## Property Value

This is a read only property whose value is a [RectangularPatternConstraint](RectangularPatternConstraint.htm).

## Version

Introduced in version September 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
# ConcentricConstraint.nativeObject Property

Parent Object: [ConcentricConstraint](ConcentricConstraint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/ConcentricConstraint.h>

## Description

The NativeObject is the object outside the context of an assembly and in the context of it's parent component. Returns null in the case where this object is not in the context of an assembly but is already the native object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"concentricConstraint\_var" is a variable referencing a ConcentricConstraint object. |

"concentricConstraint\_var" is a variable referencing a ConcentricConstraint object. ```` ``` #include <Fusion/Sketch/ConcentricConstraint.h>  // Get the value of the property. Ptr<ConcentricConstraint> propertyValue = concentricConstraint_var->nativeObject(); ``` ```` |

## Property Value

This is a read only property whose value is a [ConcentricConstraint](ConcentricConstraint.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
# PerpendicularToSurfaceConstraint.nativeObject Property

Parent Object: [PerpendicularToSurfaceConstraint](PerpendicularToSurfaceConstraint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/PerpendicularToSurfaceConstraint.h>

## Description

The NativeObject is the object outside the context of an assembly and in the context of it's parent component. Returns null in the case where this object is not in the context of an assembly but is already the native object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"perpendicularToSurfaceConstraint\_var" is a variable referencing a PerpendicularToSurfaceConstraint object. |

"perpendicularToSurfaceConstraint\_var" is a variable referencing a PerpendicularToSurfaceConstraint object. ```` ``` #include <Fusion/Sketch/PerpendicularToSurfaceConstraint.h>  // Get the value of the property. Ptr<PerpendicularToSurfaceConstraint> propertyValue = perpendicularToSurfaceConstraint_var->nativeObject(); ``` ```` |

## Property Value

This is a read only property whose value is a [PerpendicularToSurfaceConstraint](PerpendicularToSurfaceConstraint.htm).

## Version

Introduced in version September 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
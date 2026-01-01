# CoincidentToSurfaceConstraint.nativeObject Property

Parent Object: [CoincidentToSurfaceConstraint](CoincidentToSurfaceConstraint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/CoincidentToSurfaceConstraint.h>

## Description

The NativeObject is the object outside the context of an assembly and in the context of it's parent component. Returns null in the case where this object is not in the context of an assembly but is already the native object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"coincidentToSurfaceConstraint\_var" is a variable referencing a CoincidentToSurfaceConstraint object. |

"coincidentToSurfaceConstraint\_var" is a variable referencing a CoincidentToSurfaceConstraint object. ```` ``` #include <Fusion/Sketch/CoincidentToSurfaceConstraint.h>  // Get the value of the property. Ptr<CoincidentToSurfaceConstraint> propertyValue = coincidentToSurfaceConstraint_var->nativeObject(); ``` ```` |

## Property Value

This is a read only property whose value is a [CoincidentToSurfaceConstraint](CoincidentToSurfaceConstraint.htm).

## Version

Introduced in version September 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
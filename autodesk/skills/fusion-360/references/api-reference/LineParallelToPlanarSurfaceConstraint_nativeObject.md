# LineParallelToPlanarSurfaceConstraint.nativeObject Property

Parent Object: [LineParallelToPlanarSurfaceConstraint](LineParallelToPlanarSurfaceConstraint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/LineParallelToPlanarSurfaceConstraint.h>

## Description

The NativeObject is the object outside the context of an assembly and in the context of it's parent component. Returns null in the case where this object is not in the context of an assembly but is already the native object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"lineParallelToPlanarSurfaceConstraint\_var" is a variable referencing a LineParallelToPlanarSurfaceConstraint object. |

"lineParallelToPlanarSurfaceConstraint\_var" is a variable referencing a LineParallelToPlanarSurfaceConstraint object. ```` ``` #include <Fusion/Sketch/LineParallelToPlanarSurfaceConstraint.h>  // Get the value of the property. Ptr<LineParallelToPlanarSurfaceConstraint> propertyValue = lineParallelToPlanarSurfaceConstraint_var->nativeObject(); ``` ```` |

## Property Value

This is a read only property whose value is a [LineParallelToPlanarSurfaceConstraint](LineParallelToPlanarSurfaceConstraint.htm).

## Version

Introduced in version September 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
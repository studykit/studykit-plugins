# LineOnPlanarSurfaceConstraint.nativeObject Property

Parent Object: [LineOnPlanarSurfaceConstraint](LineOnPlanarSurfaceConstraint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/LineOnPlanarSurfaceConstraint.h>

## Description

The NativeObject is the object outside the context of an assembly and in the context of it's parent component. Returns null in the case where this object is not in the context of an assembly but is already the native object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"lineOnPlanarSurfaceConstraint\_var" is a variable referencing a LineOnPlanarSurfaceConstraint object. |

"lineOnPlanarSurfaceConstraint\_var" is a variable referencing a LineOnPlanarSurfaceConstraint object. ```` ``` #include <Fusion/Sketch/LineOnPlanarSurfaceConstraint.h>  // Get the value of the property. Ptr<LineOnPlanarSurfaceConstraint> propertyValue = lineOnPlanarSurfaceConstraint_var->nativeObject(); ``` ```` |

## Property Value

This is a read only property whose value is a [LineOnPlanarSurfaceConstraint](LineOnPlanarSurfaceConstraint.htm).

## Version

Introduced in version September 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
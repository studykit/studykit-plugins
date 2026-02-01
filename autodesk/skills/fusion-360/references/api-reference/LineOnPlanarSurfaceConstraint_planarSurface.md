# LineOnPlanarSurfaceConstraint.planarSurface Property

Parent Object: [LineOnPlanarSurfaceConstraint](LineOnPlanarSurfaceConstraint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/LineOnPlanarSurfaceConstraint.h>

## Description

Returns the planar BRepFace or ConstructionPlane the line is constrained to lie on.

## Syntax

* [Python](#Python)
* [C++](#C++)

"lineOnPlanarSurfaceConstraint\_var" is a variable referencing a LineOnPlanarSurfaceConstraint object. |

"lineOnPlanarSurfaceConstraint\_var" is a variable referencing a LineOnPlanarSurfaceConstraint object. ```` ``` #include <Fusion/Sketch/LineOnPlanarSurfaceConstraint.h>  // Get the value of the property. Ptr<Base> propertyValue = lineOnPlanarSurfaceConstraint_var->planarSurface(); ``` ```` |

## Property Value

This is a read only property whose value is a [Base](Base.htm).

## Version

Introduced in version September 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
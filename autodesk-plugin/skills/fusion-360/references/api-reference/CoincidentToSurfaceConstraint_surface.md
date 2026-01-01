# CoincidentToSurfaceConstraint.surface Property

Parent Object: [CoincidentToSurfaceConstraint](CoincidentToSurfaceConstraint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/CoincidentToSurfaceConstraint.h>

## Description

Returns the BRepFace or ConstructionPlane the point is constrained to.

## Syntax

* [Python](#Python)
* [C++](#C++)

"coincidentToSurfaceConstraint\_var" is a variable referencing a CoincidentToSurfaceConstraint object. |

"coincidentToSurfaceConstraint\_var" is a variable referencing a CoincidentToSurfaceConstraint object. ```` ``` #include <Fusion/Sketch/CoincidentToSurfaceConstraint.h>  // Get the value of the property. Ptr<Base> propertyValue = coincidentToSurfaceConstraint_var->surface(); ``` ```` |

## Property Value

This is a read only property whose value is a [Base](Base.htm).

## Version

Introduced in version September 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
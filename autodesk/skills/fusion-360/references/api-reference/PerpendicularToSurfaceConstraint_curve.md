# PerpendicularToSurfaceConstraint.curve Property

Parent Object: [PerpendicularToSurfaceConstraint](PerpendicularToSurfaceConstraint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/PerpendicularToSurfaceConstraint.h>

## Description

Returns the SketchCurve object that is constrained.

## Syntax

* [Python](#Python)
* [C++](#C++)

"perpendicularToSurfaceConstraint\_var" is a variable referencing a PerpendicularToSurfaceConstraint object. |

"perpendicularToSurfaceConstraint\_var" is a variable referencing a PerpendicularToSurfaceConstraint object. ```` ``` #include <Fusion/Sketch/PerpendicularToSurfaceConstraint.h>  // Get the value of the property. Ptr<SketchCurve> propertyValue = perpendicularToSurfaceConstraint_var->curve(); ``` ```` |

## Property Value

This is a read only property whose value is a [SketchCurve](SketchCurve.htm).

## Version

Introduced in version September 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
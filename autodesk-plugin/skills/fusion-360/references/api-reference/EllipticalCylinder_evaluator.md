# EllipticalCylinder.evaluator Property

Parent Object: [EllipticalCylinder](EllipticalCylinder.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/EllipticalCylinder.h>

## Description

Returns the surface evaluator.

## Syntax

* [Python](#Python)
* [C++](#C++)

"ellipticalCylinder\_var" is a variable referencing an EllipticalCylinder object. |

"ellipticalCylinder\_var" is a variable referencing an EllipticalCylinder object. ```` ``` #include <Core/Geometry/EllipticalCylinder.h>  // Get the value of the property. Ptr<SurfaceEvaluator> propertyValue = ellipticalCylinder_var->evaluator(); ``` ```` |

## Property Value

This is a read only property whose value is a [SurfaceEvaluator](SurfaceEvaluator.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
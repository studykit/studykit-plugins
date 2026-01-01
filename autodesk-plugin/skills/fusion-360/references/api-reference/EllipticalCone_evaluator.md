# EllipticalCone.evaluator Property

Parent Object: [EllipticalCone](EllipticalCone.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/EllipticalCone.h>

## Description

Returns the surface evaluator.

## Syntax

* [Python](#Python)
* [C++](#C++)

"ellipticalCone\_var" is a variable referencing an EllipticalCone object. |

"ellipticalCone\_var" is a variable referencing an EllipticalCone object. ```` ``` #include <Core/Geometry/EllipticalCone.h>  // Get the value of the property. Ptr<SurfaceEvaluator> propertyValue = ellipticalCone_var->evaluator(); ``` ```` |

## Property Value

This is a read only property whose value is a [SurfaceEvaluator](SurfaceEvaluator.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
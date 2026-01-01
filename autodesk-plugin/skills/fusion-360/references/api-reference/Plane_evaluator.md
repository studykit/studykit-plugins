# Plane.evaluator Property

Parent Object: [Plane](Plane.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Plane.h>

## Description

Returns the surface evaluator.

## Syntax

* [Python](#Python)
* [C++](#C++)

"plane\_var" is a variable referencing a Plane object. |

"plane\_var" is a variable referencing a Plane object. ```` ``` #include <Core/Geometry/Plane.h>  // Get the value of the property. Ptr<SurfaceEvaluator> propertyValue = plane_var->evaluator(); ``` ```` |

## Property Value

This is a read only property whose value is a [SurfaceEvaluator](SurfaceEvaluator.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
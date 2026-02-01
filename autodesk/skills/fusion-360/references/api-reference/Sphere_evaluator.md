# Sphere.evaluator Property

Parent Object: [Sphere](Sphere.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Sphere.h>

## Description

Returns the surface evaluator.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sphere\_var" is a variable referencing a Sphere object. |

"sphere\_var" is a variable referencing a Sphere object. ```` ``` #include <Core/Geometry/Sphere.h>  // Get the value of the property. Ptr<SurfaceEvaluator> propertyValue = sphere_var->evaluator(); ``` ```` |

## Property Value

This is a read only property whose value is a [SurfaceEvaluator](SurfaceEvaluator.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
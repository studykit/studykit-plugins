# Torus.evaluator Property

Parent Object: [Torus](Torus.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Torus.h>

## Description

Returns the surface evaluator.

## Syntax

* [Python](#Python)
* [C++](#C++)

"torus\_var" is a variable referencing a Torus object. |

"torus\_var" is a variable referencing a Torus object. ```` ``` #include <Core/Geometry/Torus.h>  // Get the value of the property. Ptr<SurfaceEvaluator> propertyValue = torus_var->evaluator(); ``` ```` |

## Property Value

This is a read only property whose value is a [SurfaceEvaluator](SurfaceEvaluator.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
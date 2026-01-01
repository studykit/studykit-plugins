# Surface.evaluator Property

Parent Object: [Surface](Surface.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Surface.h>

## Description

Returns the surface evaluator.

## Syntax

* [Python](#Python)
* [C++](#C++)

"surface\_var" is a variable referencing a Surface object. |

"surface\_var" is a variable referencing a Surface object. ```` ``` #include <Core/Geometry/Surface.h>  // Get the value of the property. Ptr<SurfaceEvaluator> propertyValue = surface_var->evaluator(); ``` ```` |

## Property Value

This is a read only property whose value is a [SurfaceEvaluator](SurfaceEvaluator.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
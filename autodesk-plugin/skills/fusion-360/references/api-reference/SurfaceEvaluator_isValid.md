# SurfaceEvaluator.isValid Property

Parent Object: [SurfaceEvaluator](SurfaceEvaluator.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/SurfaceEvaluator.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"surfaceEvaluator\_var" is a variable referencing a SurfaceEvaluator object. |

"surfaceEvaluator\_var" is a variable referencing a SurfaceEvaluator object. ```` ``` #include <Core/Geometry/SurfaceEvaluator.h>  // Get the value of the property. boolean propertyValue = surfaceEvaluator_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
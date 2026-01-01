# NurbsSurface.evaluator Property

Parent Object: [NurbsSurface](NurbsSurface.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/NurbsSurface.h>

## Description

Returns the surface evaluator.

## Syntax

* [Python](#Python)
* [C++](#C++)

"nurbsSurface\_var" is a variable referencing a NurbsSurface object. |

"nurbsSurface\_var" is a variable referencing a NurbsSurface object. ```` ``` #include <Core/Geometry/NurbsSurface.h>  // Get the value of the property. Ptr<SurfaceEvaluator> propertyValue = nurbsSurface_var->evaluator(); ``` ```` |

## Property Value

This is a read only property whose value is a [SurfaceEvaluator](SurfaceEvaluator.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
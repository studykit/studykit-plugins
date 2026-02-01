# CurveEvaluator2D.objectType Property

Parent Object: [CurveEvaluator2D](CurveEvaluator2D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/CurveEvaluator2D.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"curveEvaluator2D\_var" is a variable referencing a CurveEvaluator2D object.  ```` ``` # Get the value of the property. propertyValue = curveEvaluator2D_var.objectType ``` ```` |

"curveEvaluator2D\_var" is a variable referencing a CurveEvaluator2D object. ```` ``` #include <Core/Geometry/CurveEvaluator2D.h>  // Get the value of the property. string propertyValue = curveEvaluator2D_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
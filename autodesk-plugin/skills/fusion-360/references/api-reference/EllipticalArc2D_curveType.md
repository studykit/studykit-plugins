# EllipticalArc2D.curveType Property

Parent Object: [EllipticalArc2D](EllipticalArc2D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/EllipticalArc2D.h>

## Description

Returns the type of geometry this curve represents.

## Syntax

* [Python](#Python)
* [C++](#C++)

"ellipticalArc2D\_var" is a variable referencing an EllipticalArc2D object. |

"ellipticalArc2D\_var" is a variable referencing an EllipticalArc2D object. ```` ``` #include <Core/Geometry/EllipticalArc2D.h>  // Get the value of the property. Curve2DTypes propertyValue = ellipticalArc2D_var->curveType(); ``` ```` |

## Property Value

This is a read only property whose value is a [Curve2DTypes](Curve2DTypes.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
# Polyline2D.curveType Property

Parent Object: [Polyline2D](Polyline2D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Polyline2D.h>

## Description

Returns the type of geometry this curve represents.

## Syntax

* [Python](#Python)
* [C++](#C++)

"polyline2D\_var" is a variable referencing a Polyline2D object. |

"polyline2D\_var" is a variable referencing a Polyline2D object. ```` ``` #include <Core/Geometry/Polyline2D.h>  // Get the value of the property. Curve2DTypes propertyValue = polyline2D_var->curveType(); ``` ```` |

## Property Value

This is a read only property whose value is a [Curve2DTypes](Curve2DTypes.htm).

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
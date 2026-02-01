# Arc2D.curveType Property

Parent Object: [Arc2D](Arc2D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Arc2D.h>

## Description

Returns the type of geometry this curve represents.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arc2D\_var" is a variable referencing an Arc2D object. |

"arc2D\_var" is a variable referencing an Arc2D object. ```` ``` #include <Core/Geometry/Arc2D.h>  // Get the value of the property. Curve2DTypes propertyValue = arc2D_var->curveType(); ``` ```` |

## Property Value

This is a read only property whose value is a [Curve2DTypes](Curve2DTypes.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
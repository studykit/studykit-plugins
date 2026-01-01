# Arc3D.curveType Property

Parent Object: [Arc3D](Arc3D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Arc3D.h>

## Description

Returns the type of geometry this curve represents.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arc3D\_var" is a variable referencing an Arc3D object. |

"arc3D\_var" is a variable referencing an Arc3D object. ```` ``` #include <Core/Geometry/Arc3D.h>  // Get the value of the property. Curve3DTypes propertyValue = arc3D_var->curveType(); ``` ```` |

## Property Value

This is a read only property whose value is a [Curve3DTypes](Curve3DTypes.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
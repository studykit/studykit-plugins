# ProfileCurve.geometryType Property

Parent Object: [ProfileCurve](ProfileCurve.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/ProfileCurve.h>

## Description

Return the geometry type that the Geometry property will return.

## Syntax

* [Python](#Python)
* [C++](#C++)

"profileCurve\_var" is a variable referencing a ProfileCurve object. |

"profileCurve\_var" is a variable referencing a ProfileCurve object. ```` ``` #include <Fusion/Sketch/ProfileCurve.h>  // Get the value of the property. Curve3DTypes propertyValue = profileCurve_var->geometryType(); ``` ```` |

## Property Value

This is a read only property whose value is a [Curve3DTypes](Curve3DTypes.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
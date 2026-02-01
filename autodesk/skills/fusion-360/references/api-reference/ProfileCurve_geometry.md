# ProfileCurve.geometry Property

Parent Object: [ProfileCurve](ProfileCurve.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/ProfileCurve.h>

## Description

Returns the geometric entity of this portion of the profile.

## Syntax

* [Python](#Python)
* [C++](#C++)

"profileCurve\_var" is a variable referencing a ProfileCurve object. |

"profileCurve\_var" is a variable referencing a ProfileCurve object. ```` ``` #include <Fusion/Sketch/ProfileCurve.h>  // Get the value of the property. Ptr<Curve3D> propertyValue = profileCurve_var->geometry(); ``` ```` |

## Property Value

This is a read only property whose value is a [Curve3D](Curve3D.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
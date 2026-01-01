# PathEntity.curve Property

Parent Object: [PathEntity](PathEntity.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/PathEntity.h>

## Description

Property that returns the geometry of the entity. This is different from the original path curve if the true start point is not the same as the start point of the original path curve.

## Syntax

* [Python](#Python)
* [C++](#C++)

"pathEntity\_var" is a variable referencing a PathEntity object. |

"pathEntity\_var" is a variable referencing a PathEntity object. ```` ``` #include <Fusion/Features/PathEntity.h>  // Get the value of the property. Ptr<Curve3D> propertyValue = pathEntity_var->curve(); ``` ```` |

## Property Value

This is a read only property whose value is a [Curve3D](Curve3D.htm).

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
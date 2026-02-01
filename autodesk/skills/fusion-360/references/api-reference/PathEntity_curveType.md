# PathEntity.curveType Property

Parent Object: [PathEntity](PathEntity.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/PathEntity.h>

## Description

Property that returns the type of the curve referenced by the path entity. This property allows you to determine what type of object will be returned by the Curve property.

## Syntax

* [Python](#Python)
* [C++](#C++)

"pathEntity\_var" is a variable referencing a PathEntity object. |

"pathEntity\_var" is a variable referencing a PathEntity object. ```` ``` #include <Fusion/Features/PathEntity.h>  // Get the value of the property. Curve3DTypes propertyValue = pathEntity_var->curveType(); ``` ```` |

## Property Value

This is a read only property whose value is a [Curve3DTypes](Curve3DTypes.htm).

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
# PathEntity.isOpposedToEntity Property

Parent Object: [PathEntity](PathEntity.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/PathEntity.h>

## Description

Indicates if the orientation of this PathEntity is in the same direction or opposed to the natural direction of the SketchCurve or BRepEdge object it is derived from.

## Syntax

* [Python](#Python)
* [C++](#C++)

"pathEntity\_var" is a variable referencing a PathEntity object. |

"pathEntity\_var" is a variable referencing a PathEntity object. ```` ``` #include <Fusion/Features/PathEntity.h>  // Get the value of the property. boolean propertyValue = pathEntity_var->isOpposedToEntity(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
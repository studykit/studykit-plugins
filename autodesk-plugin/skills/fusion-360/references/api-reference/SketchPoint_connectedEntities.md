# SketchPoint.connectedEntities Property

Parent Object: [SketchPoint](SketchPoint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchPoint.h>

## Description

Returns the set of sketch entities that are directly connected to this point. For example any entities that use this point as their start point or end point will be returned and any circle, arc or ellipse who have this point as a center point will be returned. This does not include entities that are related to the point through a constraint.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchPoint\_var" is a variable referencing a SketchPoint object. |

"sketchPoint\_var" is a variable referencing a SketchPoint object. ```` ``` #include <Fusion/Sketch/SketchPoint.h>  // Get the value of the property. Ptr<SketchEntityList> propertyValue = sketchPoint_var->connectedEntities(); ``` ```` |

## Property Value

This is a read only property whose value is a [SketchEntityList](SketchEntityList.htm).

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
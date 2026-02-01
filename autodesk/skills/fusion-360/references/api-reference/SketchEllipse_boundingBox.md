# SketchEllipse.boundingBox Property

Parent Object: [SketchEllipse](SketchEllipse.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchEllipse.h>

## Description

Returns the bounding box of the entity in sketch space.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchEllipse\_var" is a variable referencing a SketchEllipse object. |

"sketchEllipse\_var" is a variable referencing a SketchEllipse object. ```` ``` #include <Fusion/Sketch/SketchEllipse.h>  // Get the value of the property. Ptr<BoundingBox3D> propertyValue = sketchEllipse_var->boundingBox(); ``` ```` |

## Property Value

This is a read only property whose value is a [BoundingBox3D](BoundingBox3D.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
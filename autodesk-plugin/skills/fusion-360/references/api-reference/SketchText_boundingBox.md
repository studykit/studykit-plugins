# SketchText.boundingBox Property

Parent Object: [SketchText](SketchText.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchText.h>

## Description

Returns the bounding box of the entity in sketch space.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchText\_var" is a variable referencing a SketchText object. |

"sketchText\_var" is a variable referencing a SketchText object. ```` ``` #include <Fusion/Sketch/SketchText.h>  // Get the value of the property. Ptr<BoundingBox3D> propertyValue = sketchText_var->boundingBox(); ``` ```` |

## Property Value

This is a read only property whose value is a [BoundingBox3D](BoundingBox3D.htm).

## Version

Introduced in version March 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
# Sketch.boundingBox Property

Parent Object: [Sketch](Sketch.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/Sketch.h>

## Description

Returns the 3D bounding box of the sketch

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketch\_var" is a variable referencing a Sketch object. |

"sketch\_var" is a variable referencing a Sketch object. ```` ``` #include <Fusion/Sketch/Sketch.h>  // Get the value of the property. Ptr<BoundingBox3D> propertyValue = sketch_var->boundingBox(); ``` ```` |

## Property Value

This is a read only property whose value is a [BoundingBox3D](BoundingBox3D.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
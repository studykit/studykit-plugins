# SketchCircle.centerSketchPoint Property

Parent Object: [SketchCircle](SketchCircle.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchCircle.h>

## Description

Returns the sketch point at the center of the circle.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchCircle\_var" is a variable referencing a SketchCircle object. |

"sketchCircle\_var" is a variable referencing a SketchCircle object. ```` ``` #include <Fusion/Sketch/SketchCircle.h>  // Get the value of the property. Ptr<SketchPoint> propertyValue = sketchCircle_var->centerSketchPoint(); ``` ```` |

## Property Value

This is a read only property whose value is a [SketchPoint](SketchPoint.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
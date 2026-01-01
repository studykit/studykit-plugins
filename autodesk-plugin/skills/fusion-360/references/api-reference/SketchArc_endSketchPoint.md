# SketchArc.endSketchPoint Property

Parent Object: [SketchArc](SketchArc.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchArc.h>

## Description

The sketch point at the end of the arc. The arc is dependent on this point and moving the point will cause the arc to adjust.

## Remarks

Sketch arcs always exist in a counterclockwise direction. If you created the sketch arc that would define a clockwise arc, the created sketch arc will be counterclockwise which means the start and end points may be opposite of what you expect.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchArc\_var" is a variable referencing a SketchArc object. |

"sketchArc\_var" is a variable referencing a SketchArc object. ```` ``` #include <Fusion/Sketch/SketchArc.h>  // Get the value of the property. Ptr<SketchPoint> propertyValue = sketchArc_var->endSketchPoint(); ``` ```` |

## Property Value

This is a read only property whose value is a [SketchPoint](SketchPoint.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
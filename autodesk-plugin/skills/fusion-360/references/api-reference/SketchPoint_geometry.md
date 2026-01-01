# SketchPoint.geometry Property

Parent Object: [SketchPoint](SketchPoint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchPoint.h>

## Description

Returns a Point3D object which provides the position of the sketch point. The returned geometry is always in sketch space.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchPoint\_var" is a variable referencing a SketchPoint object. |

"sketchPoint\_var" is a variable referencing a SketchPoint object. ```` ``` #include <Fusion/Sketch/SketchPoint.h>  // Get the value of the property. Ptr<Point3D> propertyValue = sketchPoint_var->geometry(); ``` ```` |

## Property Value

This is a read only property whose value is a [Point3D](Point3D.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
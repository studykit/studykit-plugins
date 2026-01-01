# SketchCircle.worldGeometry Property

Parent Object: [SketchCircle](SketchCircle.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchCircle.h>

## Description

Returns a Point3D object which provides the position of the sketch point in world space. The returned coordinate takes into account the assembly context and the position of the sketch in it's parent component, which means the coordinate will be returned in the root component space.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchCircle\_var" is a variable referencing a SketchCircle object. |

"sketchCircle\_var" is a variable referencing a SketchCircle object. ```` ``` #include <Fusion/Sketch/SketchCircle.h>  // Get the value of the property. Ptr<Circle3D> propertyValue = sketchCircle_var->worldGeometry(); ``` ```` |

## Property Value

This is a read only property whose value is a [Circle3D](Circle3D.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
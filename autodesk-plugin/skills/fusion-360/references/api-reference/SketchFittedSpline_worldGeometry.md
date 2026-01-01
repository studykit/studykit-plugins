# SketchFittedSpline.worldGeometry Property

Parent Object: [SketchFittedSpline](SketchFittedSpline.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchFittedSpline.h>

## Description

Returns an NurbsCurve3D object which provides geometric information in world space. The returned geometry takes into account the assembly context and the position of the sketch in it's parent component, which means the geometry will be returned in the root component space.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchFittedSpline\_var" is a variable referencing a SketchFittedSpline object. |

"sketchFittedSpline\_var" is a variable referencing a SketchFittedSpline object. ```` ``` #include <Fusion/Sketch/SketchFittedSpline.h>  // Get the value of the property. Ptr<NurbsCurve3D> propertyValue = sketchFittedSpline_var->worldGeometry(); ``` ```` |

## Property Value

This is a read only property whose value is a [NurbsCurve3D](NurbsCurve3D.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
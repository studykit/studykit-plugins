# SketchFixedSpline.geometry Property

Parent Object: [SketchFixedSpline](SketchFixedSpline.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchFixedSpline.h>

## Description

Returns the transient geometry of the curve which provides geometric information about the curve. The returned geometry is always in sketch space.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchFixedSpline\_var" is a variable referencing a SketchFixedSpline object.  ```` ``` # Get the value of the property. propertyValue = sketchFixedSpline_var.geometry ``` ```` |

"sketchFixedSpline\_var" is a variable referencing a SketchFixedSpline object. ```` ``` #include <Fusion/Sketch/SketchFixedSpline.h>  // Get the value of the property. Ptr<NurbsCurve3D> propertyValue = sketchFixedSpline_var->geometry(); ``` ```` |

## Property Value

This is a read only property whose value is a [NurbsCurve3D](NurbsCurve3D.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
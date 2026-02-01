# SketchControlPointSpline.geometry Property

Parent Object: [SketchControlPointSpline](SketchControlPointSpline.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchControlPointSpline.h>

## Description

Returns the transient geometry of the curve which provides geometric information about the curve. The returned geometry is always in sketch space. Use the worldGeometry property to get it in the model's design space.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchControlPointSpline\_var" is a variable referencing a SketchControlPointSpline object. |

"sketchControlPointSpline\_var" is a variable referencing a SketchControlPointSpline object. ```` ``` #include <Fusion/Sketch/SketchControlPointSpline.h>  // Get the value of the property. Ptr<NurbsCurve3D> propertyValue = sketchControlPointSpline_var->geometry(); ``` ```` |

## Property Value

This is a read only property whose value is a [NurbsCurve3D](NurbsCurve3D.htm).

## Version

Introduced in version July 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
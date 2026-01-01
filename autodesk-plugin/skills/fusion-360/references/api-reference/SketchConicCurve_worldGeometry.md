# SketchConicCurve.worldGeometry Property

Parent Object: [SketchConicCurve](SketchConicCurve.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchConicCurve.h>

## Description

Returns a NurbsCurve3D object that is the equivalent of this sketch curve but is in the space of the parent component rather than in sketch space.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchConicCurve\_var" is a variable referencing a SketchConicCurve object. |

"sketchConicCurve\_var" is a variable referencing a SketchConicCurve object. ```` ``` #include <Fusion/Sketch/SketchConicCurve.h>  // Get the value of the property. Ptr<NurbsCurve3D> propertyValue = sketchConicCurve_var->worldGeometry(); ``` ```` |

## Property Value

This is a read only property whose value is a [NurbsCurve3D](NurbsCurve3D.htm).

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
# SketchEllipseMajorRadiusDimension.ellipse Property

Parent Object: [SketchEllipseMajorRadiusDimension](SketchEllipseMajorRadiusDimension.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchEllipseMajorRadiusDimension.h>

## Description

Returns the ellipse or elliptical arc being constrained.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchEllipseMajorRadiusDimension\_var" is a variable referencing a SketchEllipseMajorRadiusDimension object. |

"sketchEllipseMajorRadiusDimension\_var" is a variable referencing a SketchEllipseMajorRadiusDimension object. ```` ``` #include <Fusion/Sketch/SketchEllipseMajorRadiusDimension.h>  // Get the value of the property. Ptr<SketchCurve> propertyValue = sketchEllipseMajorRadiusDimension_var->ellipse(); ``` ```` |

## Property Value

This is a read only property whose value is a [SketchCurve](SketchCurve.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
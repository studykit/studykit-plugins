# SketchEllipseMinorRadiusDimension.ellipse Property

Parent Object: [SketchEllipseMinorRadiusDimension](SketchEllipseMinorRadiusDimension.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchEllipseMinorRadiusDimension.h>

## Description

Returns the ellipse or elliptical arc being constrained.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchEllipseMinorRadiusDimension\_var" is a variable referencing a SketchEllipseMinorRadiusDimension object. |

"sketchEllipseMinorRadiusDimension\_var" is a variable referencing a SketchEllipseMinorRadiusDimension object. ```` ``` #include <Fusion/Sketch/SketchEllipseMinorRadiusDimension.h>  // Get the value of the property. Ptr<SketchCurve> propertyValue = sketchEllipseMinorRadiusDimension_var->ellipse(); ``` ```` |

## Property Value

This is a read only property whose value is a [SketchCurve](SketchCurve.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
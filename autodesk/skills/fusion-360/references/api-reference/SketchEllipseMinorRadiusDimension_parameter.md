# SketchEllipseMinorRadiusDimension.parameter Property

Parent Object: [SketchEllipseMinorRadiusDimension](SketchEllipseMinorRadiusDimension.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchEllipseMinorRadiusDimension.h>

## Description

Returns the associated parameter or null if there is no associated parameter.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchEllipseMinorRadiusDimension\_var" is a variable referencing a SketchEllipseMinorRadiusDimension object. |

"sketchEllipseMinorRadiusDimension\_var" is a variable referencing a SketchEllipseMinorRadiusDimension object. ```` ``` #include <Fusion/Sketch/SketchEllipseMinorRadiusDimension.h>  // Get the value of the property. Ptr<ModelParameter> propertyValue = sketchEllipseMinorRadiusDimension_var->parameter(); ``` ```` |

## Property Value

This is a read only property whose value is a [ModelParameter](ModelParameter.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
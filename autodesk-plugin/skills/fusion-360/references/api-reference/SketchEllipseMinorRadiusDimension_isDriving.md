# SketchEllipseMinorRadiusDimension.isDriving Property

Parent Object: [SketchEllipseMinorRadiusDimension](SketchEllipseMinorRadiusDimension.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchEllipseMinorRadiusDimension.h>

## Description

Gets and sets if the dimension is Driving or is Driven. Setting this property to true for a given dimension may fail if the result would over constrain the sketch. Fusion does not allow over-constrained sketches.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchEllipseMinorRadiusDimension\_var" is a variable referencing a SketchEllipseMinorRadiusDimension object. |

"sketchEllipseMinorRadiusDimension\_var" is a variable referencing a SketchEllipseMinorRadiusDimension object. ```` ``` #include <Fusion/Sketch/SketchEllipseMinorRadiusDimension.h>  // Get the value of the property. boolean propertyValue = sketchEllipseMinorRadiusDimension_var->isDriving();  // Set the value of the property, where value_var is a boolean. bool returnValue = sketchEllipseMinorRadiusDimension_var->isDriving(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
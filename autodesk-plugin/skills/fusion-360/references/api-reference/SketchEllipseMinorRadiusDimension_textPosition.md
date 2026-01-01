# SketchEllipseMinorRadiusDimension.textPosition Property

Parent Object: [SketchEllipseMinorRadiusDimension](SketchEllipseMinorRadiusDimension.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchEllipseMinorRadiusDimension.h>

## Description

Gets and sets position of the dimension text.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchEllipseMinorRadiusDimension\_var" is a variable referencing a SketchEllipseMinorRadiusDimension object. |

"sketchEllipseMinorRadiusDimension\_var" is a variable referencing a SketchEllipseMinorRadiusDimension object. ```` ``` #include <Fusion/Sketch/SketchEllipseMinorRadiusDimension.h>  // Get the value of the property. Ptr<Point3D> propertyValue = sketchEllipseMinorRadiusDimension_var->textPosition();  // Set the value of the property, where value_var is a Point3D. bool returnValue = sketchEllipseMinorRadiusDimension_var->textPosition(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Point3D](Point3D.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
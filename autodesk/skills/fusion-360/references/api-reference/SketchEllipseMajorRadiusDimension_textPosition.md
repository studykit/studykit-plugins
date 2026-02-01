# SketchEllipseMajorRadiusDimension.textPosition Property

Parent Object: [SketchEllipseMajorRadiusDimension](SketchEllipseMajorRadiusDimension.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchEllipseMajorRadiusDimension.h>

## Description

Gets and sets position of the dimension text.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchEllipseMajorRadiusDimension\_var" is a variable referencing a SketchEllipseMajorRadiusDimension object. |

"sketchEllipseMajorRadiusDimension\_var" is a variable referencing a SketchEllipseMajorRadiusDimension object. ```` ``` #include <Fusion/Sketch/SketchEllipseMajorRadiusDimension.h>  // Get the value of the property. Ptr<Point3D> propertyValue = sketchEllipseMajorRadiusDimension_var->textPosition();  // Set the value of the property, where value_var is a Point3D. bool returnValue = sketchEllipseMajorRadiusDimension_var->textPosition(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Point3D](Point3D.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
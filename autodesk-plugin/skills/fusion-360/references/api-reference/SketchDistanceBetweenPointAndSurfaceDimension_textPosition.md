# SketchDistanceBetweenPointAndSurfaceDimension.textPosition Property

Parent Object: [SketchDistanceBetweenPointAndSurfaceDimension](SketchDistanceBetweenPointAndSurfaceDimension.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchDistanceBetweenPointAndSurfaceDimension.h>

## Description

Gets and sets position of the dimension text.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchDistanceBetweenPointAndSurfaceDimension\_var" is a variable referencing a SketchDistanceBetweenPointAndSurfaceDimension object. |

"sketchDistanceBetweenPointAndSurfaceDimension\_var" is a variable referencing a SketchDistanceBetweenPointAndSurfaceDimension object. ```` ``` #include <Fusion/Sketch/SketchDistanceBetweenPointAndSurfaceDimension.h>  // Get the value of the property. Ptr<Point3D> propertyValue = sketchDistanceBetweenPointAndSurfaceDimension_var->textPosition();  // Set the value of the property, where value_var is a Point3D. bool returnValue = sketchDistanceBetweenPointAndSurfaceDimension_var->textPosition(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Point3D](Point3D.htm).

## Version

Introduced in version September 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
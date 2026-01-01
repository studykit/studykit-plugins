# SketchRadialDimension.textPosition Property

Parent Object: [SketchRadialDimension](SketchRadialDimension.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchRadialDimension.h>

## Description

Gets and sets position of the dimension text.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchRadialDimension\_var" is a variable referencing a SketchRadialDimension object. |

"sketchRadialDimension\_var" is a variable referencing a SketchRadialDimension object. ```` ``` #include <Fusion/Sketch/SketchRadialDimension.h>  // Get the value of the property. Ptr<Point3D> propertyValue = sketchRadialDimension_var->textPosition();  // Set the value of the property, where value_var is a Point3D. bool returnValue = sketchRadialDimension_var->textPosition(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Point3D](Point3D.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
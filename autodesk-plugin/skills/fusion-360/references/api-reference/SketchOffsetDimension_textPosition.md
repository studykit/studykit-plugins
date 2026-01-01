# SketchOffsetDimension.textPosition Property

Parent Object: [SketchOffsetDimension](SketchOffsetDimension.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchOffsetDimension.h>

## Description

Gets and sets position of the dimension text.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchOffsetDimension\_var" is a variable referencing a SketchOffsetDimension object. |

"sketchOffsetDimension\_var" is a variable referencing a SketchOffsetDimension object. ```` ``` #include <Fusion/Sketch/SketchOffsetDimension.h>  // Get the value of the property. Ptr<Point3D> propertyValue = sketchOffsetDimension_var->textPosition();  // Set the value of the property, where value_var is a Point3D. bool returnValue = sketchOffsetDimension_var->textPosition(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Point3D](Point3D.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
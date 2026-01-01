# SketchDiameterDimension.textPosition Property

Parent Object: [SketchDiameterDimension](SketchDiameterDimension.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchDiameterDimension.h>

## Description

Gets and sets position of the dimension text.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchDiameterDimension\_var" is a variable referencing a SketchDiameterDimension object. |

"sketchDiameterDimension\_var" is a variable referencing a SketchDiameterDimension object. ```` ``` #include <Fusion/Sketch/SketchDiameterDimension.h>  // Get the value of the property. Ptr<Point3D> propertyValue = sketchDiameterDimension_var->textPosition();  // Set the value of the property, where value_var is a Point3D. bool returnValue = sketchDiameterDimension_var->textPosition(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Point3D](Point3D.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
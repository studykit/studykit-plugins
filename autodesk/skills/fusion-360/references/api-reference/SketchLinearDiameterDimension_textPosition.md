# SketchLinearDiameterDimension.textPosition Property

Parent Object: [SketchLinearDiameterDimension](SketchLinearDiameterDimension.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchLinearDiameterDimension.h>

## Description

Gets and sets position of the dimension text.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchLinearDiameterDimension\_var" is a variable referencing a SketchLinearDiameterDimension object. |

"sketchLinearDiameterDimension\_var" is a variable referencing a SketchLinearDiameterDimension object. ```` ``` #include <Fusion/Sketch/SketchLinearDiameterDimension.h>  // Get the value of the property. Ptr<Point3D> propertyValue = sketchLinearDiameterDimension_var->textPosition();  // Set the value of the property, where value_var is a Point3D. bool returnValue = sketchLinearDiameterDimension_var->textPosition(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Point3D](Point3D.htm).

## Version

Introduced in version September 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
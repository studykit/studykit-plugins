# SketchLinearDiameterDimension.isDriving Property

Parent Object: [SketchLinearDiameterDimension](SketchLinearDiameterDimension.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchLinearDiameterDimension.h>

## Description

Gets and sets if the dimension is Driving or is Driven. Setting this property to true for a given dimension may fail if the result would over constrain the sketch. Fusion does not allow over-constrained sketches.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchLinearDiameterDimension\_var" is a variable referencing a SketchLinearDiameterDimension object. |

"sketchLinearDiameterDimension\_var" is a variable referencing a SketchLinearDiameterDimension object. ```` ``` #include <Fusion/Sketch/SketchLinearDiameterDimension.h>  // Get the value of the property. boolean propertyValue = sketchLinearDiameterDimension_var->isDriving();  // Set the value of the property, where value_var is a boolean. bool returnValue = sketchLinearDiameterDimension_var->isDriving(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version September 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
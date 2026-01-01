# SketchDiameterDimension.isDriving Property

Parent Object: [SketchDiameterDimension](SketchDiameterDimension.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchDiameterDimension.h>

## Description

Gets and sets if the dimension is Driving or is Driven. Setting this property to true for a given dimension may fail if the result would over constrain the sketch. Fusion does not allow over-constrained sketches.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchDiameterDimension\_var" is a variable referencing a SketchDiameterDimension object. |

"sketchDiameterDimension\_var" is a variable referencing a SketchDiameterDimension object. ```` ``` #include <Fusion/Sketch/SketchDiameterDimension.h>  // Get the value of the property. boolean propertyValue = sketchDiameterDimension_var->isDriving();  // Set the value of the property, where value_var is a boolean. bool returnValue = sketchDiameterDimension_var->isDriving(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
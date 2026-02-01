# SketchConcentricCircleDimension.isDriving Property

Parent Object: [SketchConcentricCircleDimension](SketchConcentricCircleDimension.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchConcentricCircleDimension.h>

## Description

Gets and sets if the dimension is Driving or is Driven. Setting this property to true for a given dimension may fail if the result would over constrain the sketch. Fusion does not allow over-constrained sketches.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchConcentricCircleDimension\_var" is a variable referencing a SketchConcentricCircleDimension object. |

"sketchConcentricCircleDimension\_var" is a variable referencing a SketchConcentricCircleDimension object. ```` ``` #include <Fusion/Sketch/SketchConcentricCircleDimension.h>  // Get the value of the property. boolean propertyValue = sketchConcentricCircleDimension_var->isDriving();  // Set the value of the property, where value_var is a boolean. bool returnValue = sketchConcentricCircleDimension_var->isDriving(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
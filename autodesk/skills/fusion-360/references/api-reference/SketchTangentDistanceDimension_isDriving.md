# SketchTangentDistanceDimension.isDriving Property

Parent Object: [SketchTangentDistanceDimension](SketchTangentDistanceDimension.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchTangentDistanceDimension.h>

## Description

Gets and sets if the dimension is Driving or is Driven. Setting this property to true for a given dimension may fail if the result would over constrain the sketch. Fusion does not allow over-constrained sketches.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchTangentDistanceDimension\_var" is a variable referencing a SketchTangentDistanceDimension object. |

"sketchTangentDistanceDimension\_var" is a variable referencing a SketchTangentDistanceDimension object. ```` ``` #include <Fusion/Sketch/SketchTangentDistanceDimension.h>  // Get the value of the property. boolean propertyValue = sketchTangentDistanceDimension_var->isDriving();  // Set the value of the property, where value_var is a boolean. bool returnValue = sketchTangentDistanceDimension_var->isDriving(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version July 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
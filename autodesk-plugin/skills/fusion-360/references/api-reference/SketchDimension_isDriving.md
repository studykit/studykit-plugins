# SketchDimension.isDriving Property

Parent Object: [SketchDimension](SketchDimension.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchDimension.h>

## Description

Gets and sets if the dimension is Driving or is Driven. Setting this property to true for a given dimension may fail if the result would over constrain the sketch. Fusion does not allow over-constrained sketches.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchDimension\_var" is a variable referencing a SketchDimension object. |

"sketchDimension\_var" is a variable referencing a SketchDimension object. ```` ``` #include <Fusion/Sketch/SketchDimension.h>  // Get the value of the property. boolean propertyValue = sketchDimension_var->isDriving();  // Set the value of the property, where value_var is a boolean. bool returnValue = sketchDimension_var->isDriving(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
# SketchDistanceBetweenPointAndSurfaceDimension.isDriving Property

Parent Object: [SketchDistanceBetweenPointAndSurfaceDimension](SketchDistanceBetweenPointAndSurfaceDimension.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchDistanceBetweenPointAndSurfaceDimension.h>

## Description

Gets and sets if the dimension is Driving or is Driven. Setting this property to true for a given dimension may fail if the result would over constrain the sketch. Fusion does not allow over-constrained sketches.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchDistanceBetweenPointAndSurfaceDimension\_var" is a variable referencing a SketchDistanceBetweenPointAndSurfaceDimension object. |

"sketchDistanceBetweenPointAndSurfaceDimension\_var" is a variable referencing a SketchDistanceBetweenPointAndSurfaceDimension object. ```` ``` #include <Fusion/Sketch/SketchDistanceBetweenPointAndSurfaceDimension.h>  // Get the value of the property. boolean propertyValue = sketchDistanceBetweenPointAndSurfaceDimension_var->isDriving();  // Set the value of the property, where value_var is a boolean. bool returnValue = sketchDistanceBetweenPointAndSurfaceDimension_var->isDriving(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version September 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
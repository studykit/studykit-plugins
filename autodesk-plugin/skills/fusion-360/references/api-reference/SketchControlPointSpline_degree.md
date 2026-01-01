# SketchControlPointSpline.degree Property

Parent Object: [SketchControlPointSpline](SketchControlPointSpline.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchControlPointSpline.h>

## Description

Gets and sets the degree of the spline.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchControlPointSpline\_var" is a variable referencing a SketchControlPointSpline object. |

"sketchControlPointSpline\_var" is a variable referencing a SketchControlPointSpline object. ```` ``` #include <Fusion/Sketch/SketchControlPointSpline.h>  // Get the value of the property. SplineDegrees propertyValue = sketchControlPointSpline_var->degree();  // Set the value of the property, where value_var is a SplineDegrees. bool returnValue = sketchControlPointSpline_var->degree(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [SplineDegrees](SplineDegrees.htm).

## Version

Introduced in version July 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
# SketchControlPointSpline.isFixed Property

Parent Object: [SketchControlPointSpline](SketchControlPointSpline.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchControlPointSpline.h>

## Description

Indicates if this geometry is "fixed".

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchControlPointSpline\_var" is a variable referencing a SketchControlPointSpline object. |

"sketchControlPointSpline\_var" is a variable referencing a SketchControlPointSpline object. ```` ``` #include <Fusion/Sketch/SketchControlPointSpline.h>  // Get the value of the property. boolean propertyValue = sketchControlPointSpline_var->isFixed();  // Set the value of the property, where value_var is a boolean. bool returnValue = sketchControlPointSpline_var->isFixed(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version July 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
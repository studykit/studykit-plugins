# SketchCurve.isConstruction Property

Parent Object: [SketchCurve](SketchCurve.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchCurve.h>

## Description

Gets and sets whether this curve is construction geometry.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchCurve\_var" is a variable referencing a SketchCurve object. |

"sketchCurve\_var" is a variable referencing a SketchCurve object. ```` ``` #include <Fusion/Sketch/SketchCurve.h>  // Get the value of the property. boolean propertyValue = sketchCurve_var->isConstruction();  // Set the value of the property, where value_var is a boolean. bool returnValue = sketchCurve_var->isConstruction(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
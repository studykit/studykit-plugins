# SketchConicCurve.rhoValue Property

Parent Object: [SketchConicCurve](SketchConicCurve.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchConicCurve.h>

## Description

Get and sets the rho value for the curve. The value must be greater than zero and less than one.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchConicCurve\_var" is a variable referencing a SketchConicCurve object. |

"sketchConicCurve\_var" is a variable referencing a SketchConicCurve object. ```` ``` #include <Fusion/Sketch/SketchConicCurve.h>  // Get the value of the property. double propertyValue = sketchConicCurve_var->rhoValue();  // Set the value of the property, where value_var is a double. bool returnValue = sketchConicCurve_var->rhoValue(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version May 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
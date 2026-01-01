# SketchConicCurve.isFixed Property

Parent Object: [SketchConicCurve](SketchConicCurve.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchConicCurve.h>

## Description

Indicates if this geometry is "fixed".

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchConicCurve\_var" is a variable referencing a SketchConicCurve object. |

"sketchConicCurve\_var" is a variable referencing a SketchConicCurve object. ```` ``` #include <Fusion/Sketch/SketchConicCurve.h>  // Get the value of the property. boolean propertyValue = sketchConicCurve_var->isFixed();  // Set the value of the property, where value_var is a boolean. bool returnValue = sketchConicCurve_var->isFixed(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
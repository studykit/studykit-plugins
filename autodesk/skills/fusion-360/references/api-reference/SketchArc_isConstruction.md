# SketchArc.isConstruction Property

Parent Object: [SketchArc](SketchArc.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchArc.h>

## Description

Gets and sets whether this curve is construction geometry.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchArc\_var" is a variable referencing a SketchArc object. |

"sketchArc\_var" is a variable referencing a SketchArc object. ```` ``` #include <Fusion/Sketch/SketchArc.h>  // Get the value of the property. boolean propertyValue = sketchArc_var->isConstruction();  // Set the value of the property, where value_var is a boolean. bool returnValue = sketchArc_var->isConstruction(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
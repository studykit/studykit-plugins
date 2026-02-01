# SketchEllipticalArc.majorAxisRadius Property

Parent Object: [SketchEllipticalArc](SketchEllipticalArc.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchEllipticalArc.h>

## Description

Gets and sets the major axis radius of the elliptical arc. Changing the radius is limited by any constraints that might exist on the elliptical arc. Setting the radius can fail in cases where the radius is fully defined through constraints.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchEllipticalArc\_var" is a variable referencing a SketchEllipticalArc object. |

"sketchEllipticalArc\_var" is a variable referencing a SketchEllipticalArc object. ```` ``` #include <Fusion/Sketch/SketchEllipticalArc.h>  // Get the value of the property. double propertyValue = sketchEllipticalArc_var->majorAxisRadius();  // Set the value of the property, where value_var is a double. bool returnValue = sketchEllipticalArc_var->majorAxisRadius(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
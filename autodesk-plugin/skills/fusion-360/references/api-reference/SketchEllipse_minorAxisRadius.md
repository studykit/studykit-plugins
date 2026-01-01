# SketchEllipse.minorAxisRadius Property

Parent Object: [SketchEllipse](SketchEllipse.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchEllipse.h>

## Description

Gets and sets the minor axis radius of the ellipse. Changing the radius is limited by any constraints that might exist on the ellipse. Setting the radius can fail in cases where the radius is fully defined through constraints.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchEllipse\_var" is a variable referencing a SketchEllipse object. |

"sketchEllipse\_var" is a variable referencing a SketchEllipse object. ```` ``` #include <Fusion/Sketch/SketchEllipse.h>  // Get the value of the property. double propertyValue = sketchEllipse_var->minorAxisRadius();  // Set the value of the property, where value_var is a double. bool returnValue = sketchEllipse_var->minorAxisRadius(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
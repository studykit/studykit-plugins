# SketchCircle.radius Property

Parent Object: [SketchCircle](SketchCircle.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchCircle.h>

## Description

Gets and sets the radius of the circle. Changing the radius is limited by any constraints that might exist on the circle.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchCircle\_var" is a variable referencing a SketchCircle object. |

"sketchCircle\_var" is a variable referencing a SketchCircle object. ```` ``` #include <Fusion/Sketch/SketchCircle.h>  // Get the value of the property. double propertyValue = sketchCircle_var->radius();  // Set the value of the property, where value_var is a double. bool returnValue = sketchCircle_var->radius(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
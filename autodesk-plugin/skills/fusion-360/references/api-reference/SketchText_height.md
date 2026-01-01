# SketchText.height Property

Parent Object: [SketchText](SketchText.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchText.h>

## Description

Gets and sets the height of the text in centimeters.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchText\_var" is a variable referencing a SketchText object. |

"sketchText\_var" is a variable referencing a SketchText object. ```` ``` #include <Fusion/Sketch/SketchText.h>  // Get the value of the property. double propertyValue = sketchText_var->height();  // Set the value of the property, where value_var is a double. bool returnValue = sketchText_var->height(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version March 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
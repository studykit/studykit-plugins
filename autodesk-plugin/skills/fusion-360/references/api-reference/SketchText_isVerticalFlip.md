# SketchText.isVerticalFlip Property

Parent Object: [SketchText](SketchText.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchText.h>

## Description

Gets and sets if the text is flipped vertically.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchText\_var" is a variable referencing a SketchText object. |

"sketchText\_var" is a variable referencing a SketchText object. ```` ``` #include <Fusion/Sketch/SketchText.h>  // Get the value of the property. boolean propertyValue = sketchText_var->isVerticalFlip();  // Set the value of the property, where value_var is a boolean. bool returnValue = sketchText_var->isVerticalFlip(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version December 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
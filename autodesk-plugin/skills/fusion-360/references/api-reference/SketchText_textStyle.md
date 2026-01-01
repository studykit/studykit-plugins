# SketchText.textStyle Property

Parent Object: [SketchText](SketchText.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchText.h>

## Description

Gets and sets the text style to apply to the entire text. This is a bitwise enum so styles can be combined to apply multiple styles. For example you can apply bold and underline.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchText\_var" is a variable referencing a SketchText object. |

"sketchText\_var" is a variable referencing a SketchText object. ```` ``` #include <Fusion/Sketch/SketchText.h>  // Get the value of the property. TextStyles propertyValue = sketchText_var->textStyle();  // Set the value of the property, where value_var is a TextStyles. bool returnValue = sketchText_var->textStyle(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [TextStyles](TextStyles.htm).

## Version

Introduced in version March 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
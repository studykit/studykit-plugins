# SketchTextInput.textStyle Property

Parent Object: [SketchTextInput](SketchTextInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchTextInput.h>

## Description

Gets and sets the text style to apply to the entire text. This is a bitwise enum so styles can be combined to apply multiple styles. For example you can apply bold and italic.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchTextInput\_var" is a variable referencing a SketchTextInput object. |

"sketchTextInput\_var" is a variable referencing a SketchTextInput object. ```` ``` #include <Fusion/Sketch/SketchTextInput.h>  // Get the value of the property. TextStyles propertyValue = sketchTextInput_var->textStyle();  // Set the value of the property, where value_var is a TextStyles. bool returnValue = sketchTextInput_var->textStyle(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [TextStyles](TextStyles.htm).

## Version

Introduced in version March 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
# SketchTextInput.text Property

Parent Object: [SketchTextInput](SketchTextInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchTextInput.h>

## Description

Gets and sets the text.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchTextInput\_var" is a variable referencing a SketchTextInput object. |

"sketchTextInput\_var" is a variable referencing a SketchTextInput object. ```` ``` #include <Fusion/Sketch/SketchTextInput.h>  // Get the value of the property. string propertyValue = sketchTextInput_var->text();  // Set the value of the property, where value_var is a string. bool returnValue = sketchTextInput_var->text(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version March 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
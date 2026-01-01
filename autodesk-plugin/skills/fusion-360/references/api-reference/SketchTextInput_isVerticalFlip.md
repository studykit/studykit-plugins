# SketchTextInput.isVerticalFlip Property

Parent Object: [SketchTextInput](SketchTextInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchTextInput.h>

## Description

Gets and sets if the text is flipped vertically.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchTextInput\_var" is a variable referencing a SketchTextInput object. |

"sketchTextInput\_var" is a variable referencing a SketchTextInput object. ```` ``` #include <Fusion/Sketch/SketchTextInput.h>  // Get the value of the property. boolean propertyValue = sketchTextInput_var->isVerticalFlip();  // Set the value of the property, where value_var is a boolean. bool returnValue = sketchTextInput_var->isVerticalFlip(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Sketch Text API Sample](SketchTextSample_Sample.htm) | Demonstrates creating sketch text by creating both mult-line text and text along a curve. |

## Version

Introduced in version December 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
# Sketch.sketchTexts Property

Parent Object: [Sketch](Sketch.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/Sketch.h>

## Description

Returns the sketch text collection associated with this sketch. This provides access to existing text and supports the creation of new text.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketch\_var" is a variable referencing a Sketch object. |

"sketch\_var" is a variable referencing a Sketch object. ```` ``` #include <Fusion/Sketch/Sketch.h>  // Get the value of the property. Ptr<SketchTexts> propertyValue = sketch_var->sketchTexts(); ``` ```` |

## Property Value

This is a read only property whose value is a [SketchTexts](SketchTexts.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [SketchTextInput.setAsAlongPath](SketchTextinput_setAsAlongPath_Sample.htm) | Demonstrates the SketchTextInput.setAsAlongPath method. |
| [Sketch Text API Sample](SketchTextSample_Sample.htm) | Demonstrates creating sketch text by creating both mult-line text and text along a curve. |

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
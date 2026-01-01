# SketchTexts.add Method

Parent Object: [SketchTexts](SketchTexts.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchTexts.h>

## Description

Creates a sketch text.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchTexts\_var" is a variable referencing a [SketchTexts](SketchTexts.htm) object.```` ``` returnValue = sketchTexts_var.add(input) ``` ```` |

"sketchTexts\_var" is a variable referencing a [SketchTexts](SketchTexts.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [SketchText](SketchText.htm) | Returns the newly created SketchText object or null in the case of failure. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| input | [SketchTextInput](SketchTextInput.htm) | A SketchTextInput object created using the SketchTexts.createInput method. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [SketchTextInput.setAsAlongPath](SketchTextinput_setAsAlongPath_Sample.htm) | Demonstrates the SketchTextInput.setAsAlongPath method. |
| [SketchTextInput.setAsFitOnPath](SketchTextInput_setAsFitOnPath_Sample.htm) | Demoonstrates the SketchTextInput.setAsFitOnPath method. |
| [SketchTextInput.setAsMultiLine](SketchTextInput_setAsMultiLine_Sample.htm) | Demonstrates the SketchTextInput.setAsMultiLine method. |
| [Sketch Text API Sample](SketchTextSample_Sample.htm) | Demonstrates creating sketch text by creating both mult-line text and text along a curve. |

## Version

Introduced in version March 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
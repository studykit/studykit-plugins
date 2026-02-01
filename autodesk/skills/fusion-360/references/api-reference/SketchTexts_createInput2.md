# SketchTexts.createInput2 Method

Parent Object: [SketchTexts](SketchTexts.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchTexts.h>

## Description

Creates a SketchTextInput object that is used to define the additional input to create text. The SketchTextInput object is equivalent to the Sketch Text dialog in that it collects all of the input required to create sketch text. You must call setAsFitOnPath, setAsAlongPath, or setAsMultiLine methods to define one of the three types of text and can use other and define any setAs Once the properties of the SketchTextInput object have been defined, use the add method to create the sketch text.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchTexts\_var" is a variable referencing a [SketchTexts](SketchTexts.htm) object.```` ``` returnValue = sketchTexts_var.createInput2(formattedText, height) ``` ```` |

"sketchTexts\_var" is a variable referencing a [SketchTexts](SketchTexts.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [SketchTextInput](SketchTextInput.htm) | Returns a SketchTextInput object that can be used to set additional formatting and is used as input to the add method. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| formattedText | string | The text used for the sketch text. This is a simple string as no additional formatting is currently supported. |
| height | double | The height of the text in centimeters. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [SketchTextInput.setAsAlongPath](SketchTextinput_setAsAlongPath_Sample.htm) | Demonstrates the SketchTextInput.setAsAlongPath method. |
| [SketchTextInput.setAsFitOnPath](SketchTextInput_setAsFitOnPath_Sample.htm) | Demoonstrates the SketchTextInput.setAsFitOnPath method. |
| [SketchTextInput.setAsMultiLine](SketchTextInput_setAsMultiLine_Sample.htm) | Demonstrates the SketchTextInput.setAsMultiLine method. |
| [Sketch Text API Sample](SketchTextSample_Sample.htm) | Demonstrates creating sketch text by creating both mult-line text and text along a curve. |

## Version

Introduced in version December 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
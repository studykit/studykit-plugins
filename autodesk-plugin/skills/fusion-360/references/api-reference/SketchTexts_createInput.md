# SketchTexts.createInput Method

Parent Object: [SketchTexts](SketchTexts.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchTexts.h>

## Description

This function is retired. See more information in the 'Remarks' section below.

## Remarks

This method has been retired and is replaced by the createInput2 method, which supports defining multi-line text and text along a curve.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchTexts\_var" is a variable referencing a [SketchTexts](SketchTexts.htm) object.```` ``` returnValue = sketchTexts_var.createInput(formattedText, height, position) ``` ```` |

"sketchTexts\_var" is a variable referencing a [SketchTexts](SketchTexts.htm) object.  ```` ``` #include <Fusion/Sketch/SketchTexts.h>  returnValue = sketchTexts_var->createInput(formattedText, height, position); ``` ```` |

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
| position | [Point3D](Point3D.htm) | The position of the text on the x-y plane of the sketch. The text must lie on the x-y plane so the Z component of the point is ignored and always treated as zero. |

## Version

Introduced in version March 2015
Retired in version January 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
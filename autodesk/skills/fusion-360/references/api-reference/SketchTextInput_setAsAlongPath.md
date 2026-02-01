# SketchTextInput.setAsAlongPath Method

Parent Object: [SketchTextInput](SketchTextInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchTextInput.h>

## Description

Sets this SketchTextInput to define text that follows along a specified path.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchTextInput\_var" is a variable referencing a [SketchTextInput](SketchTextInput.htm) object.```` ``` returnValue = sketchTextInput_var.setAsAlongPath(path, isAbovePath, horizontalAlignment, characterSpacing) ``` ```` |

"sketchTextInput\_var" is a variable referencing a [SketchTextInput](SketchTextInput.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the setting the definition was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| path | [Base](Base.htm) | The entity that defines the path for the text. This can be a SketchCurve or BRepEdge object. |
| isAbovePath | boolean | Indicates if the text should be positioned above or below the path entity. |
| horizontalAlignment | [HorizontalAlignments](HorizontalAlignments.htm) | Specifies the horizontal alignment of the text with respect to the path curve. |
| characterSpacing | double | The percentage change in default spacing between characters. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [SketchTextInput.setAsAlongPath](SketchTextinput_setAsAlongPath_Sample.htm) | Demonstrates the SketchTextInput.setAsAlongPath method. |
| [Sketch Text API Sample](SketchTextSample_Sample.htm) | Demonstrates creating sketch text by creating both mult-line text and text along a curve. |

## Version

Introduced in version December 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
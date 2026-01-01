# SketchText.redefineAsAlongPath Method

Parent Object: [SketchText](SketchText.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchText.h>

## Description

Sets this SketchTextInput to define text that follows along a specified path.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchText\_var" is a variable referencing a [SketchText](SketchText.htm) object.```` ``` returnValue = sketchText_var.redefineAsAlongPath(path, isAbovePath, horizontalAlignment, characterSpacing) ``` ```` |

"sketchText\_var" is a variable referencing a [SketchText](SketchText.htm) object. |

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
| characterSpacing | double | The spacing between the characters. This is an additional spacing to apply that is defined as a percentage of the default spacing. A spacing of 0 indicates no additional spacing. A spacing of 50 indicates to use the default plus 50% of the default. |

## Version

Introduced in version December 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
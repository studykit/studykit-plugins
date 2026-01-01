# SketchText.redefineAsFitOnPath Method

Parent Object: [SketchText](SketchText.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchText.h>

## Description

Sets this SketchTextInput to define text that fits along a specified path. Fitting on a path will space the characters so the text fits along the entire length of the path entity.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchText\_var" is a variable referencing a [SketchText](SketchText.htm) object.```` ``` returnValue = sketchText_var.redefineAsFitOnPath(path, isAbovePath) ``` ```` |

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

## Version

Introduced in version December 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
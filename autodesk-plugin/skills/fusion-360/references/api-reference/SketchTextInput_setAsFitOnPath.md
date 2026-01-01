# SketchTextInput.setAsFitOnPath Method

Parent Object: [SketchTextInput](SketchTextInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchTextInput.h>

## Description

Sets this SketchTextInput to define text that fits along a specified path. Fitting on a path will space the characters so the text fits along the entire length of the path entity.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchTextInput\_var" is a variable referencing a [SketchTextInput](SketchTextInput.htm) object.```` ``` returnValue = sketchTextInput_var.setAsFitOnPath(path, isAbovePath) ``` ```` |

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

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [SketchTextInput.setAsFitOnPath](SketchTextInput_setAsFitOnPath_Sample.htm) | Demoonstrates the SketchTextInput.setAsFitOnPath method. |

## Version

Introduced in version December 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
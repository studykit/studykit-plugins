# SketchText.asCurves Method

Parent Object: [SketchText](SketchText.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchText.h>

## Description

Returns the underlying curves that define the outline of the text. Calling this does not affect the SketchText and does not create any new sketch geometry but returns the geometrical definition of the sketch outline.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchText\_var" is a variable referencing a [SketchText](SketchText.htm) object.```` ``` returnValue = sketchText_var.asCurves() ``` ```` |

"sketchText\_var" is a variable referencing a [SketchText](SketchText.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Curve3D](Curve3D.htm)[] | Returns an array of transient curves that represent the outline of the text. |

## Version

Introduced in version August 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
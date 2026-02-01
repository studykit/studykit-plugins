# SketchText.explode Method

Parent Object: [SketchText](SketchText.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchText.h>

## Description

Explodes the SketchText into a set of curves. The original SketchText is deleted as a result of calling this.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchText\_var" is a variable referencing a [SketchText](SketchText.htm) object.```` ``` returnValue = sketchText_var.explode() ``` ```` |

"sketchText\_var" is a variable referencing a [SketchText](SketchText.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [SketchCurve](SketchCurve.htm)[] | Returns an array of the sketch curves that were created that represent the text. |

## Version

Introduced in version August 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
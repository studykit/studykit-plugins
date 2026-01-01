# SketchPoint.move Method

Parent Object: [SketchPoint](SketchPoint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchPoint.h>

## Description

Moves the sketch geometry using the specified transform. Move respects any constraints that would normally prohibit the move. This will fail in the case where the IsReference property is true.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchPoint\_var" is a variable referencing a [SketchPoint](SketchPoint.htm) object.```` ``` returnValue = sketchPoint_var.move(translation) ``` ```` |

"sketchPoint\_var" is a variable referencing a [SketchPoint](SketchPoint.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if moving the sketch point was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| translation | [Vector3D](Vector3D.htm) | The vector that defines the distance and direction to move. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Sketch Point API Sample](SketchPointSample_Sample.htm) | Demonstrates creating a new sketch point. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
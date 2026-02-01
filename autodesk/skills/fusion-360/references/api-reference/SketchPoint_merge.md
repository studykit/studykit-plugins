# SketchPoint.merge Method

Parent Object: [SketchPoint](SketchPoint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchPoint.h>

## Description

Merges the input sketch point into this sketch point. This effectively deletes the other sketch point and changes all entities that referenced that sketch point to reference this sketch point.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchPoint\_var" is a variable referencing a [SketchPoint](SketchPoint.htm) object.```` ``` returnValue = sketchPoint_var.merge(point) ``` ```` |

"sketchPoint\_var" is a variable referencing a [SketchPoint](SketchPoint.htm) object.  ```` ``` #include <Fusion/Sketch/SketchPoint.h>  returnValue = sketchPoint_var->merge(point); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the merge was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| point | [SketchPoint](SketchPoint.htm) | The point to merge with this point. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
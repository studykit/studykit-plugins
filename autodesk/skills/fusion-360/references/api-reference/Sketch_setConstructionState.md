# Sketch.setConstructionState Method

Parent Object: [Sketch](Sketch.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/Sketch.h>

## Description

Method that sets the Construction state for an array of sketch curves.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketch\_var" is a variable referencing a [Sketch](Sketch.htm) object.```` ``` returnValue = sketch_var.setConstructionState(sketchCurves, constructionState) ``` ```` |

"sketch\_var" is a variable referencing a [Sketch](Sketch.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| sketchCurves | SketchCurve[] | An array of sketch curves to set the construction status. |
| constructionState | [SketchCurveConstructionStates](SketchCurveConstructionStates.htm) | Input enum value that specifies if the construction state of the input curves should be toggled, set to construction, or set to normal. |

## Version

Introduced in version March 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
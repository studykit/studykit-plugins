# Sketch.setCenterlineState Method

Parent Object: [Sketch](Sketch.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/Sketch.h>

## Description

Method that sets the Centerline state for an array of sketch lines.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketch\_var" is a variable referencing a [Sketch](Sketch.htm) object.```` ``` returnValue = sketch_var.setCenterlineState(sketchLines, centerlineState) ``` ```` |

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
| sketchLines | SketchLine[] | An array of sketch lines to set the centerline status |
| centerlineState | [SketchLineCenterlineStates](SketchLineCenterlineStates.htm) | Input enum value that specifies if the centerline state of the input lines should be toggled, set to centerline, or set to normal |

## Version

Introduced in version March 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
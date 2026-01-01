# Sketch.findConnectedCurves Method

Parent Object: [Sketch](Sketch.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/Sketch.h>

## Description

Finds the sketch curves that are end connected to the input curve. This can be useful for many cases but is especially useful in gathering the input when creating an offset.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketch\_var" is a variable referencing a [Sketch](Sketch.htm) object.```` ``` returnValue = sketch_var.findConnectedCurves(curve) ``` ```` |

"sketch\_var" is a variable referencing a [Sketch](Sketch.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ObjectCollection](ObjectCollection.htm) | A collection of the connected curves. They are returned in their connected order with the original input curve being one of the curves. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| curve | [SketchCurve](SketchCurve.htm) | The initial sketch curve that will be used to find the connected curves. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Sketch fillet and offset API Sample](SketchFilletAndOffset_Sample.htm) | Demonstrates the creation of a fillet in a sketch and offset a set of curves. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
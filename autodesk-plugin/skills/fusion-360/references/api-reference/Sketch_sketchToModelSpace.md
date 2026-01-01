# Sketch.sketchToModelSpace Method

Parent Object: [Sketch](Sketch.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/Sketch.h>

## Description

A specified point in sketch space returns the equivalent point in model space. This is sensitive to the assembly context.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketch\_var" is a variable referencing a [Sketch](Sketch.htm) object.```` ``` returnValue = sketch_var.sketchToModelSpace(sketchCoordinate) ``` ```` |

"sketch\_var" is a variable referencing a [Sketch](Sketch.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Point3D](Point3D.htm) | Returns the equivalent point in model space. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| sketchCoordinate | [Point3D](Point3D.htm) | A coordinate in sketch space. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
# Sketch.projectCutEdges Method

Parent Object: [Sketch](Sketch.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/Sketch.h>

## Description

Intersects the specified body with the sketch plane and creates new curves representing the intersection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketch\_var" is a variable referencing a [Sketch](Sketch.htm) object.```` ``` returnValue = sketch_var.projectCutEdges(body) ``` ```` |

"sketch\_var" is a variable referencing a [Sketch](Sketch.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ObjectCollection](ObjectCollection.htm) | Returns a collection of the sketch entities that were created a a result of the cut. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| body | [BRepBody](BRepBody.htm) | The body to be intersected by the sketch. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
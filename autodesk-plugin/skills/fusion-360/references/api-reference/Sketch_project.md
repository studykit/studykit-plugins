# Sketch.project Method

Parent Object: [Sketch](Sketch.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/Sketch.h>

## Description

This function is retired. See more information in the 'Remarks' section below.

## Remarks

Projects the specified entity or entities onto the x-y plane of the sketch and returns the created sketch entity(s). You can provide either a single entity or an ObjectCollection of multiple entities, which will be projected simultaneously.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketch\_var" is a variable referencing a [Sketch](Sketch.htm) object.```` ``` returnValue = sketch_var.project(entity) ``` ```` |

"sketch\_var" is a variable referencing a [Sketch](Sketch.htm) object.  ```` ``` #include <Fusion/Sketch/Sketch.h>  returnValue = sketch_var->project(entity); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ObjectCollection](ObjectCollection.htm) | Returns a collection of the sketch entities that were created as a result of the projection. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| entity | [Base](Base.htm) | The entity to project. This can be a single entity of the following types: sketch entity, an edge, a face (which will get all of its edges), a vertex, a construction axis, a construction point, or a construction plane that is perpendicular to the sketch to create a line.   This can also be an ObjectCollection that contains multiple entities and will be projected simultaneously. The entities that can be projected must be the types and have the same restrictions as described above. |

## Version

Introduced in version August 2014
Retired in version May 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
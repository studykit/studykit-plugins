# RipFeatureInput.setBetweenPoints Method

Parent Object: [RipFeatureInput](RipFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/RipFeatureInput.h>

## Description

This input method is for creating a rip between two points. Each point can be either a BRepVertex or a BRepEdge and an associated offset along the edge.

## Syntax

* [Python](#Python)
* [C++](#C++)

"ripFeatureInput\_var" is a variable referencing a [RipFeatureInput](RipFeatureInput.htm) object.```` ``` # Uses no optional arguments. ``` ```` |

"ripFeatureInput\_var" is a variable referencing a [RipFeatureInput](RipFeatureInput.htm) object.  ```` ``` #include <Fusion/SheetMetal/RipFeatureInput.h>  // Uses no optional arguments. returnValue = ripFeatureInput_var->setBetweenPoints(pointOneEntity, pointTwoEntity, gapDistance);  // Uses optional arguments. returnValue = ripFeatureInput_var->setBetweenPoints(pointOneEntity, pointTwoEntity, gapDistance, pointOneOffset, pointTwoOffset); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the rip definition is successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| pointOneEntity | [Base](Base.htm) | The first point of the rip. This can be defined using a BrepVertex or a BRepEdge and offset to define where the point is along the edge. If an edge is specified, the pointOneOffset parameter must be specified. |
| pointTwoEntity | [Base](Base.htm) | The second point of the rip and must lie on the same face as point 1. This can be defined using a BrepVertex or a BRepEdge and an offset to define where the point is along the edge. If an edge is specified, the pointTwoOffset parameter must be specified. |
| gapDistance | [ValueInput](ValueInput.htm) | The gap distance of the rip. |
| pointOneOffset | [ValueInput](ValueInput.htm) | If the first point lies on an edge, then this is the offset along the edge which defines the point. This is the physical distance from the topological start of the edge. If the offset is negative or exceeds the edge length, the corresponding vertex of the edge will be used.   This is an optional argument whose default value is null. |
| pointTwoOffset | [ValueInput](ValueInput.htm) | If the second point lies on an edge, then this is the offset along the edge which defines the point. This is the physical distance from the topological start of the edge. If the offset is negative or exceeds the edge length, the corresponding vertex of the edge will be used.   This is an optional argument whose default value is null. |

## Version

Introduced in version September 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
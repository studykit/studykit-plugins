# HoleFeature.setPositionOnEdge Method

Parent Object: [HoleFeature](HoleFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/HoleFeature.h>

## Description

Redefines the position and orientation of the hole to be on the start, end or center of an edge.

## Syntax

* [Python](#Python)
* [C++](#C++)

"holeFeature\_var" is a variable referencing a [HoleFeature](HoleFeature.htm) object.```` ``` returnValue = holeFeature_var.setPositionOnEdge(planarEntity, edge, position) ``` ```` |

"holeFeature\_var" is a variable referencing a [HoleFeature](HoleFeature.htm) object.  ```` ``` #include <Fusion/Features/HoleFeature.h>  returnValue = holeFeature_var->setPositionOnEdge(planarEntity, edge, position); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| planarEntity | [Base](Base.htm) | The planar BRepFace or ConstructionPlane object that defines the orientation of the hole and start of the hole. The natural direction of the hole will be opposite the normal of the face or construction plane. |
| edge | [BRepEdge](BRepEdge.htm) | The edge to position the hole on. |
| position | [HoleEdgePositions](HoleEdgePositions.htm) | The position along the edge to place the hole. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
# BRepCoEdgeDefinitions.add Method

Parent Object: [BRepCoEdgeDefinitions](BRepCoEdgeDefinitions.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepCoEdgeDefinitions.h>

## Description

Creates a new BrepCoEdgeDefinition object associated with the parent BrepLoopDefinition object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepCoEdgeDefinitions\_var" is a variable referencing a [BRepCoEdgeDefinitions](BRepCoEdgeDefinitions.htm) object.```` ``` returnValue = bRepCoEdgeDefinitions_var.add(edgeDefinition, isOpposedToEdge) ``` ```` |

"bRepCoEdgeDefinitions\_var" is a variable referencing a [BRepCoEdgeDefinitions](BRepCoEdgeDefinitions.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [BRepCoEdgeDefinition](BRepCoEdgeDefinition.htm) | Returns the newly created BrepCoEdgeDefinition object or null in the case of failure. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| edgeDefinition | [BRepEdgeDefinition](BRepEdgeDefinition.htm) | The BRepEdgeDefinition object this co-edge is related to. |
| isOpposedToEdge | boolean | Boolean that indicates if the orientation of this BRepCoEdgeDefinition is reversed with respect to the associated BRepEdgeDefinition object. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [BRep Body definition Sample](BRepBodyDefinition_Sample.htm) | Demonstrates creating BRep bodies by BRepBodyDefinition. |

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
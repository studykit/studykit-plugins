# BRepBodyDefinition.createVertexDefinition Method

Parent Object: [BRepBodyDefinition](BRepBodyDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepBodyDefinition.h>

## Description

Creates a new BRepVertexDefinition object that's associated with the body.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepBodyDefinition\_var" is a variable referencing a [BRepBodyDefinition](BRepBodyDefinition.htm) object.```` ``` returnValue = bRepBodyDefinition_var.createVertexDefinition(position) ``` ```` |

"bRepBodyDefinition\_var" is a variable referencing a [BRepBodyDefinition](BRepBodyDefinition.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [BRepVertexDefinition](BRepVertexDefinition.htm) | Returns the created BRepVertexDefinition object or null in the case of failure. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| position | [Point3D](Point3D.htm) | Specifies the position of the vertex in model space. |

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
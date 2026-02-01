# BRepEdge.createForAssemblyContext Method

Parent Object: [BRepEdge](BRepEdge.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepEdge.h>

## Description

Returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepEdge\_var" is a variable referencing a [BRepEdge](BRepEdge.htm) object.```` ``` returnValue = bRepEdge_var.createForAssemblyContext(occurrence) ``` ```` |

"bRepEdge\_var" is a variable referencing a [BRepEdge](BRepEdge.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [BRepEdge](BRepEdge.htm) | Returns the new BrepEdge proxy or null if this isn't the NativeObject. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| occurrence | [Occurrence](Occurrence.htm) | The occurrence that defines the context for the created proxy. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
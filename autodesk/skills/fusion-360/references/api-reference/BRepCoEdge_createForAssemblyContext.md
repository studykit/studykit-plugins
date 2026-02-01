# BRepCoEdge.createForAssemblyContext Method

Parent Object: [BRepCoEdge](BRepCoEdge.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepCoEdge.h>

## Description

Returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepCoEdge\_var" is a variable referencing a [BRepCoEdge](BRepCoEdge.htm) object.```` ``` returnValue = bRepCoEdge_var.createForAssemblyContext(occurrence) ``` ```` |

"bRepCoEdge\_var" is a variable referencing a [BRepCoEdge](BRepCoEdge.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [BRepCoEdge](BRepCoEdge.htm) | Returns the new BrepCoEdge proxy or null if this isn't the NativeObject. |

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
# BRepVertex.createForAssemblyContext Method

Parent Object: [BRepVertex](BRepVertex.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepVertex.h>

## Description

Returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepVertex\_var" is a variable referencing a [BRepVertex](BRepVertex.htm) object.```` ``` returnValue = bRepVertex_var.createForAssemblyContext(occurrence) ``` ```` |

"bRepVertex\_var" is a variable referencing a [BRepVertex](BRepVertex.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [BRepVertex](BRepVertex.htm) | Returns the new BrepVertex proxy or null if this isn't the NativeObject. |

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
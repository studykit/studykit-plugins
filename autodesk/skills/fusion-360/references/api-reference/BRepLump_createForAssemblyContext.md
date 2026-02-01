# BRepLump.createForAssemblyContext Method

Parent Object: [BRepLump](BRepLump.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepLump.h>

## Description

Returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepLump\_var" is a variable referencing a [BRepLump](BRepLump.htm) object.```` ``` returnValue = bRepLump_var.createForAssemblyContext(occurrence) ``` ```` |

"bRepLump\_var" is a variable referencing a [BRepLump](BRepLump.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [BRepLump](BRepLump.htm) | Returns the new BrepLump proxy or null if this isn't the NativeObject. |

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
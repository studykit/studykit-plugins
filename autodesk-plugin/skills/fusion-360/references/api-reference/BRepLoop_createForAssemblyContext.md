# BRepLoop.createForAssemblyContext Method

Parent Object: [BRepLoop](BRepLoop.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepLoop.h>

## Description

Returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepLoop\_var" is a variable referencing a [BRepLoop](BRepLoop.htm) object.```` ``` returnValue = bRepLoop_var.createForAssemblyContext(occurrence) ``` ```` |

"bRepLoop\_var" is a variable referencing a [BRepLoop](BRepLoop.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [BRepLoop](BRepLoop.htm) | Returns the new BrepLoop proxy or null if this isn't the NativeObject. |

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
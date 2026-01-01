# BRepFace.createForAssemblyContext Method

Parent Object: [BRepFace](BRepFace.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepFace.h>

## Description

Returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepFace\_var" is a variable referencing a [BRepFace](BRepFace.htm) object.```` ``` returnValue = bRepFace_var.createForAssemblyContext(occurrence) ``` ```` |

"bRepFace\_var" is a variable referencing a [BRepFace](BRepFace.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [BRepFace](BRepFace.htm) | Returns the new BRepFace proxy or null if this isn't the NativeObject. |

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
# BRepBody.createForAssemblyContext Method

Parent Object: [BRepBody](BRepBody.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepBody.h>

## Description

Returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepBody\_var" is a variable referencing a [BRepBody](BRepBody.htm) object.```` ``` returnValue = bRepBody_var.createForAssemblyContext(occurrence) ``` ```` |

"bRepBody\_var" is a variable referencing a [BRepBody](BRepBody.htm) object.  ```` ``` #include <Fusion/BRep/BRepBody.h>  returnValue = bRepBody_var->createForAssemblyContext(occurrence); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [BRepBody](BRepBody.htm) | Returns the new BRepBoy proxy or null if this isn't the NativeObject. |

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
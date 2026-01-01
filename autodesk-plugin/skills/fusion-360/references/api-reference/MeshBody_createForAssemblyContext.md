# MeshBody.createForAssemblyContext Method

Parent Object: [MeshBody](MeshBody.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/MeshBody/MeshBody.h>

## Description

Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence. Fails if this object is not the NativeObject.

## Syntax

* [Python](#Python)
* [C++](#C++)

"meshBody\_var" is a variable referencing a [MeshBody](MeshBody.htm) object.```` ``` returnValue = meshBody_var.createForAssemblyContext(occurrence) ``` ```` |

"meshBody\_var" is a variable referencing a [MeshBody](MeshBody.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [MeshBody](MeshBody.htm) | Returns the proxy for the occurrence in the context of the specified occurrence. Returns null if it failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| occurrence | [Occurrence](Occurrence.htm) | The occurrence that represents the context you want to create this proxy in. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
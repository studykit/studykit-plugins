# PatchFeature.createForAssemblyContext Method

Parent Object: [PatchFeature](PatchFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/PatchFeature.h>

## Description

Creates or returns a proxy for the native object - i.e., a new object that represents this object but adds the assembly context defined by the input occurrence.

## Syntax

* [Python](#Python)
* [C++](#C++)

"patchFeature\_var" is a variable referencing a [PatchFeature](PatchFeature.htm) object.```` ``` returnValue = patchFeature_var.createForAssemblyContext(occurrence) ``` ```` |

"patchFeature\_var" is a variable referencing a [PatchFeature](PatchFeature.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [PatchFeature](PatchFeature.htm) | Returns the proxy object or null if this is not the NativeObject. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| occurrence | [Occurrence](Occurrence.htm) | The occurrence that defines the context to create the proxy. |

## Version

Introduced in version July 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
# MirrorFeature.createForAssemblyContext Method

Parent Object: [MirrorFeature](MirrorFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/MirrorFeature.h>

## Description

Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence.

## Syntax

* [Python](#Python)
* [C++](#C++)

"mirrorFeature\_var" is a variable referencing a [MirrorFeature](MirrorFeature.htm) object.```` ``` returnValue = mirrorFeature_var.createForAssemblyContext(occurrence) ``` ```` |

"mirrorFeature\_var" is a variable referencing a [MirrorFeature](MirrorFeature.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [MirrorFeature](MirrorFeature.htm) | Returns the proxy object or null if this isn't the NativeObject. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| occurrence | [Occurrence](Occurrence.htm) | The occurrence that defines the context to create the proxy in. |

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
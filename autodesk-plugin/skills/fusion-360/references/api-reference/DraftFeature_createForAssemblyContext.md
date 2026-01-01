# DraftFeature.createForAssemblyContext Method

Parent Object: [DraftFeature](DraftFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/DraftFeature.h>

## Description

Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence.

## Syntax

* [Python](#Python)
* [C++](#C++)

"draftFeature\_var" is a variable referencing a [DraftFeature](DraftFeature.htm) object.```` ``` returnValue = draftFeature_var.createForAssemblyContext(occurrence) ``` ```` |

"draftFeature\_var" is a variable referencing a [DraftFeature](DraftFeature.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [DraftFeature](DraftFeature.htm) | Returns the proxy object or null if this isn't the NativeObject. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| occurrence | [Occurrence](Occurrence.htm) | The occurrence that defines the context to create the proxy in. |

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
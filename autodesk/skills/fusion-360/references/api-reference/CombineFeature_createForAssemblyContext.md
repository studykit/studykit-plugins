# CombineFeature.createForAssemblyContext Method

Parent Object: [CombineFeature](CombineFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/CombineFeature.h>

## Description

Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence.

## Syntax

* [Python](#Python)
* [C++](#C++)

"combineFeature\_var" is a variable referencing a [CombineFeature](CombineFeature.htm) object.```` ``` returnValue = combineFeature_var.createForAssemblyContext(occurrence) ``` ```` |

"combineFeature\_var" is a variable referencing a [CombineFeature](CombineFeature.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [CombineFeature](CombineFeature.htm) | Returns the proxy object or null if this isn't the NativeObject. |

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
# TrimFeature.createForAssemblyContext Method

Parent Object: [TrimFeature](TrimFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/TrimFeature.h>

## Description

Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence.

## Syntax

* [Python](#Python)
* [C++](#C++)

"trimFeature\_var" is a variable referencing a [TrimFeature](TrimFeature.htm) object.```` ``` returnValue = trimFeature_var.createForAssemblyContext(occurrence) ``` ```` |

"trimFeature\_var" is a variable referencing a [TrimFeature](TrimFeature.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [TrimFeature](TrimFeature.htm) | Returns the proxy object or null if this isn't the NativeObject. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| occurrence | [Occurrence](Occurrence.htm) | The occurrence that defines the context to create the proxy in. |

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
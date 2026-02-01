# UntrimFeature.createForAssemblyContext Method

Parent Object: [UntrimFeature](UntrimFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/UntrimFeature.h>

## Description

Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence.

## Syntax

* [Python](#Python)
* [C++](#C++)

"untrimFeature\_var" is a variable referencing a [UntrimFeature](UntrimFeature.htm) object.```` ``` returnValue = untrimFeature_var.createForAssemblyContext(occurrence) ``` ```` |

"untrimFeature\_var" is a variable referencing a [UntrimFeature](UntrimFeature.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [UntrimFeature](UntrimFeature.htm) | Returns the proxy object or null if this is not the NativeObject. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| occurrence | [Occurrence](Occurrence.htm) | The occurrence that defines the context to create the proxy in. |

## Version

Introduced in version January 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
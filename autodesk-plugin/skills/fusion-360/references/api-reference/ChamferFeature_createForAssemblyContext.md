# ChamferFeature.createForAssemblyContext Method

Parent Object: [ChamferFeature](ChamferFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ChamferFeature.h>

## Description

Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence.

## Syntax

* [Python](#Python)
* [C++](#C++)

"chamferFeature\_var" is a variable referencing a [ChamferFeature](ChamferFeature.htm) object.```` ``` returnValue = chamferFeature_var.createForAssemblyContext(occurrence) ``` ```` |

"chamferFeature\_var" is a variable referencing a [ChamferFeature](ChamferFeature.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ChamferFeature](ChamferFeature.htm) | Returns the proxy object or null if this isn't the NativeObject. |

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
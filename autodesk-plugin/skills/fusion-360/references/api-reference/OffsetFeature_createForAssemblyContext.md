# OffsetFeature.createForAssemblyContext Method

Parent Object: [OffsetFeature](OffsetFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/OffsetFeature.h>

## Description

Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence.

## Syntax

* [Python](#Python)
* [C++](#C++)

"offsetFeature\_var" is a variable referencing an [OffsetFeature](OffsetFeature.htm) object.```` ``` returnValue = offsetFeature_var.createForAssemblyContext(occurrence) ``` ```` |

"offsetFeature\_var" is a variable referencing an [OffsetFeature](OffsetFeature.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [OffsetFeature](OffsetFeature.htm) | Returns the proxy object or null if this is not the NativeObject. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| occurrence | [Occurrence](Occurrence.htm) | The occurrence that defines the context to create the proxy in. |

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
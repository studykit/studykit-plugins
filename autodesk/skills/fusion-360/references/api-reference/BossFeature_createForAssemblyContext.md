# BossFeature.createForAssemblyContext Method

Parent Object: [BossFeature](BossFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Plastic/BossFeature.h>

## Description

Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bossFeature\_var" is a variable referencing a [BossFeature](BossFeature.htm) object.```` ``` returnValue = bossFeature_var.createForAssemblyContext(occurrence) ``` ```` |

"bossFeature\_var" is a variable referencing a [BossFeature](BossFeature.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [BossFeature](BossFeature.htm) | Returns the proxy object or null if this isn't the NativeObject. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| occurrence | [Occurrence](Occurrence.htm) | The occurrence that defines the context to create the proxy in. |

## Version

Introduced in version October 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |